import os

import mysql.connector.pooling
from MySQLdb import Error
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class MysqlDatabase:
    def __init__(self, logger):
        self.logger = logger

        self.dbconfig = {
            "database": os.environ.get("mysql_db"),
            "user": os.environ.get("mysql_user"),
            "host": os.environ.get("mysql_host"),
            "port": os.environ.get("mysql_port"),
            "password": os.environ.get("mysql_pass")
        }

        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mysql_pool",
                                                                pool_size=6,
                                                                **self.dbconfig)
        self.logger.info(f"[DATABASE] [mysql] Connection Pool Setup")

    def get_connection(self):
        connection = self.pool.get_connection()
        self.logger.info(f"[DATABASE] [mysql] new PoolConnection: thread {connection.connection_id}")
        return connection

    def database_query_with_debug(self, query):
        pool = self.get_connection()
        cursor = None
        database = ""
        try:
            if pool.is_connected():
                self.logger.info("Connected to MySQL database using connection pool")

                cursor = pool.cursor()
                cursor.execute(query)
                pool.commit()

                split_query = query.split(" ")
                for i in range(len(split_query)):
                    if split_query[i].lower() == "from":
                        database = split_query[i + 1]
                        break
                    elif split_query[i].lower() == "into":
                        database = split_query[i + 1]
                        break
                    elif split_query[i].lower() == "update":
                        database = split_query[i + 1]
                        break

                cursor.execute("SELECT * from " + database + " LIMIT 5")
                record = cursor.fetchall()

                self.logger.info(f"Your Mother connected to - {record}")

        except Error as e:
            self.logger.debug("Error while connecting to MySQL using Connection pool ", e)
        finally:
            # closing database connection.
            if pool.is_connected():
                cursor.close()
                pool.close()
                self.logger.info("MySQL connection has been closed")
