import json

from tabulate import tabulate


class OrdersMenuHandler:
    def __init__(self, dcm):
        self.db = dcm

        self.orderTypes = [
            "DECLINED",
            "CONFIRMED",
            "PENDING"]

        self.defaultlist = [
            ['Return to Main Menu', 0],
            ['PRINT orders list', 1],
            ['CREATE new order', 2],
            ['UPDATE existing order status', 3],
            ['UPDATE existing order', 4],
            ['DELETE order', 5]
        ]
        self.OrderDict = []
        self.KVDict = {}
        print(tabulate(self.defaultlist, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))

        # print(self.dcm)
        for item in self.db.getDB()["orders"]:
            index = self.db.getDB()["orders"].index(item)
            index += 1
            self.KVDict[index] = item
            # print(f"Adding: k:{index}, v:{item}")
            self.OrderDict.append([item, index])

        self.open_menu(int(input("please input your order option: ") or "0"))

    def open_menu(self, _input):
        # regenerate the self.OrderDict using the below function to get the new values from the database file
        self.recreate_list()

        if _input == 5:
            # STRETCH GOAL - DELETE order
            print(tabulate(self.OrderDict, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))
            self.remove_from_db(int(input("please input your order you want to delete: ")))
            self.default_return()

        if _input == 4:
            # # STRETCH - UPDATE existing order
            print(tabulate(self.OrderDict, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))
            order_id = int(input("please input your order id to update: "))
            order_name = input("please input your new order name [default: press enter]: ") or "default"
            order_address = input("please input your new order Address [default: press enter]: ") or "default"
            order_phone_number = input("please input your new order phoneNumber [default: press enter]: ") or "default"
            self.update_order_by_id(order_id, name=order_name, address=order_address, PhoneNumber=order_phone_number)
            print(tabulate(self.OrderDict, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
            self.default_return()

        elif _input == 3:
            # STRETCH GOAL - UPDATE existing product
            print(tabulate(self.OrderDict, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))
            order_id = int(input("please input your order id to update: "))
            print(f"order \nid: type\n {json.dumps(self.orderTypes, indent=2, sort_keys=True)}")
            order_status_id = int(input("please input your new order status id: "))
            self.update_order_status_by_id(order_id, order_status_id)
            self.default_return()

        elif _input == 2:
            # Create Order
            self.create_order(input("please input your name: "), input("please input your address: "),
                              input("please input your Phone Number: "))
            print(tabulate(self.OrderDict, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
            self.default_return()

        elif _input == 1:
            # PRINT products list
            print(tabulate(self.OrderDict, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
            self.default_return()

        elif _input == 0:
            # RETURN to main menu
            return 0

    def create_order(self, name, address, phone_number):
        self.db.getDB()["orders"].append({"name": name, "address": address, "PhoneNumber": phone_number, "status": self.orderTypes[1]})
        self.db.writeFile()
        self.recreate_list()

    def update_order_status_by_id(self, index, types):
        self.db.getDB()["orders"][index - 1].update({"status": self.orderTypes[types]})
        self.db.writeFile()
        self.recreate_list()

    def update_order_by_id(self, index, **kwargs):
        for key, value in kwargs.items():
            if not value == "default":
                self.db.getDB()["orders"][index - 1].update({f"{key}": value})
        self.db.writeFile()
        self.recreate_list()

    def remove_from_db(self, index):
        print(f"index: {index - 1}, removedItem: {self.db.getDB()['orders'][index - 1]}")
        self.db.getDB()["orders"].pop(index - 1)
        self.db.writeFile()
        self.recreate_list()

    def recreate_list(self):
        self.OrderDict.clear()
        self.KVDict = {}
        # print(self.dcm)
        for item in self.db.getDB()["orders"]:
            index = self.db.getDB()["orders"].index(item)
            index += 1
            self.KVDict[index] = item
            # print(f"Adding: k:{index}, v:{item}")
            self.OrderDict.append([item, index])

    def __repr__(self):
        return 0

    def default_return(self):
        self.recreate_list()
        print(tabulate(self.defaultlist, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
        self.open_menu(int(input("please input your order option: ") or "0"))
