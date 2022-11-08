import json
import os
import sys

databaseFile = "database.json"


class JsonDatabase:
    def __init__(self):
        self.db = {
            "products": [],
            "orders": [],
            "couriers": []
        }

        if self.checkExists(databaseFile):
            self.readFile()
        else:
            self.writeFile()
            self.readFile()

    def write_path(self, path, value):
        # string split
        curr = {}
        for key in path:
            if key not in curr:
                curr[key] = {}
            curr = curr[key]
        k, v = value
        curr[k] = v
        self.db.update(curr)
        self.writeFile()

    def getDB(self):
        return self.db

    def checkExists(self, file):
        return os.path.exists(os.getcwd() + os.sep + file)

    def readFile(self):
        with open(databaseFile) as database_file:
            self.db = json.load(database_file)

    def writeFile(self):
        with open(databaseFile, "w") as outfile:
            outfile.write(json.dumps(self.db, indent=2, sort_keys=True))

        self.readFile()
