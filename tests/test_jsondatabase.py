import os
import unittest
from random import randint

from Objects.Couriers import Couriers
from Objects.Order import Order
from Objects.Product import Product
from utils.JsonDatabase import JsonDatabase

database = JsonDatabase("tests/test_db.json")
database.writeFile()

products = Product(database)
orders = Order(database)
couriers = Couriers(database)


def normalise_path(path):
    return os.getcwd() + os.sep + path.replace("/", os.sep).replace("\\", os.sep)


def check_file_exists(file):
    return os.path.exists(normalise_path(file))


class TestDatabase(unittest.TestCase):
    def test_dbfile(self):
        self.assertEqual(check_file_exists("tests/test_db.json"), True)

    def test_add_product(self):
        products.create_product("item1", float(randint(0, 10)))
        productout = products.get_product_by_id(0)["name"] == "item1"
        self.assertEqual(productout, True)

    def test_delete_db(self):
        os.remove(normalise_path("tests/test_db.json"))
        self.assertEqual(check_file_exists("tests/test_db.json"), False)


if __name__ == '__main__':
    unittest.main()
