from tabulate import tabulate

from utils.Logging import Logging


class Product:
    def __init__(self, db):
        self.DEBUG = False
        self.db = db
        self.ProductDict = []
        self.logUtil = Logging("Products", False)
        self.regenerate_products()

    def getProducts(self):
        return self.ProductDict

    def print_products(self):
        print(tabulate(self.ProductDict, headers=['Product Management Manu', 'Option Number'], tablefmt="outline"))

    def create_product(self, name, price):
        self.db.getDB()["products"].append({
            "name": name,
            "price": price,
        })
        self.db.writeFile()
        self.db.readFile()
        self.regenerate_products()

    def update_product_by_id(self, index, **kwargs):
        for key, value in kwargs.items():
            if not value == "default":
                self.db.getDB()["products"][index - 1].update({f"{key}": value})
        self.db.writeFile()
        self.db.readFile()
        self.regenerate_products()

    def remove_from_db(self, index):
        if self.check_within_range(self.db.getDB()['products'], index):
            print(f"index: {index - 1}, removedItem: {self.db.getDB()['products'][index - 1]}")
            self.db.getDB()["products"].pop(index - 1)
            self.db.writeFile()
            self.db.readFile()
            self.regenerate_products()
        else:
            print(f"please use a value between [1 and {self.db.getDB()['products'].__len__()}]")

    def regenerate_products(self):
        self.ProductDict.clear()
        # print(self.dcm)
        for item in self.db.getDB()["products"]:
            index = self.db.getDB()["products"].index(item)
            index += 1
            self.ProductDict.append([item, index])

    def get_product_by_id(self, product_id):
        return self.db.getDB()["products"][product_id]

    # check if given value is within items index range
    def check_within_range(self, _object, index):
        if self.DEBUG:
            print(
                f"_object: {_object} \n"
                f"index: {index}, \n"
                f"_object.__len__(): {_object.__len__()}"
            )
        if (index > (_object.__len__() + 1)) or (index < 1):
            if self.DEBUG:
                print("not in Range")
            return False
        else:
            if self.DEBUG:
                print("in Range")
            return True
