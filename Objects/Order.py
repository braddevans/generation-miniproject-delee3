from random import randint

from tabulate import tabulate

from Objects.Couriers import Couriers
from utils.Logging import Logging


class Order:
    def __init__(self, db):
        self.DEBUG = False
        self.db = db
        self.OrderDict = []
        self.logUtil = Logging("Order", False)
        self.couriers = Couriers(self.db)
        self.orderTypes = [
            "PENDING",
            "DECLINED",
            "CONFIRMED"
        ]

    def getOrders(self):
        return self.OrderDict

    def print_orders(self):
        print(tabulate(self.OrderDict, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))

    def create_order(self, name, address, phone_number):
        self.db.getDB()["orders"].append({
            "customer_name": name,
            "customer_address": address,
            "customer_phone": phone_number,
            "courier": None,
            "status": self.orderTypes[0],
            "items": [],
            "created_at": self.logUtil.timestamp()
        })
        self.db.writeFile()
        self.regenerate_orders()

    def assign_random_courier(self, order_id):
        self.db.getDB()["orders"][order_id - 1].update({"courier": randint(0, self.couriers.getCouriers().__len__() - 1)})
        self.db.writeFile()

    def add_items_to_order_by_id(self, order_id, items):
        db_items = self.db.getDB()["orders"][order_id - 1]["items"]
        for item in items:
            db_items.append(item)

        print(db_items)
        self.db.getDB()["orders"][order_id - 1].update({"items": db_items})
        self.db.writeFile()

    def get_order_by_id(self, order_id):
        return self.db.getDB()["orders"][order_id - 1]

    def update_order_status_by_id(self, index, types):
        if self.check_within_range(self.orderTypes, types):
            self.db.getDB()["orders"][index - 1].update({"status": self.orderTypes[types - 1]})
            self.db.writeFile()
            self.regenerate_orders()
        else:
            print(f"please use a value between [1 and {self.orderTypes.__len__()}]")

    def update_order_by_id(self, index, **kwargs):
        for key, value in kwargs.items():
            if not value == "default":
                self.db.getDB()["orders"][index - 1].update({f"{key}": value})
        self.db.getDB()["orders"][index - 1].update({"updated_at": self.logUtil.timestamp()})
        self.db.writeFile()
        self.regenerate_orders()

    def remove_from_db(self, index):
        if self.check_within_range(self.db.getDB()['orders'], index):
            print(f"index: {index - 1}, removedItem: {self.db.getDB()['orders'][index - 1]}")
            self.db.getDB()["orders"].pop(index - 1)
            self.db.writeFile()
            self.regenerate_orders()
        else:
            print(f"please use a value between [1 and {self.db.getDB()['orders'].__len__()}]")

    def regenerate_orders(self):
        self.OrderDict.clear()
        # print(self.dcm)
        for item in self.db.getDB()["orders"]:
            index = self.db.getDB()["orders"].index(item)
            index += 1
            self.OrderDict.append([item, index])

    def getTypes(self):
        return self.orderTypes

    def print_order_items_by_order_id(self, order_id):
        order = self.get_order_by_id(order_id)
        items = order["items"]
        item_list = []

        for item in items:
            prod = self.db.getDB()["products"][int(item) - 1]
            index = int(item) - 1
            index += 1
            item_list.append([prod, index])
        print(tabulate(item_list, headers=['Item List Manu', 'Option Number'], tablefmt="outline"))

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
