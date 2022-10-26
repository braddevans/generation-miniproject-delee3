import json

from tabulate import tabulate


class OrdersMenuHandler:
    def __init__(self, dcm):
        self.db = dcm

        self.orderTypes = {
            0: "DECLINED",
            1: "CONFIRMED",
            2: "PENDING"
        }

        self.defaultlist = [
            ['Return to Main Menu', 0],
            ['PRINT orders list', 1],
            ['CREATE new order', 2],
            ['UPDATE existing order status', 3],
            ['UPDATE existing order', 4],
            ['DELETE order', 5]
        ]
        self.Orderdictlist = []
        self.kvdict = {}
        print(tabulate(self.defaultlist, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))

        # print(self.dcm)
        for item in self.db.getDB()["orders"]:
            index = self.db.getDB()["orders"].index(item)
            index += 1
            self.kvdict[index] = item
            # print(f"Adding: k:{index}, v:{item}")
            self.Orderdictlist.append([item, index])

        self.open_menu(int(input("please input your order option: ") or "0"))

    def open_menu(self, _input):
        self.recreate_list()
        if _input == 5:
            # STRETCH GOAL - DELETE order
            # PRINT orders list
            # GET user input for order index value
            # DELETE order at index in order list
            print(tabulate(self.Orderdictlist, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))
            self.remove_from_db(int(input("please input your order you want to delete: ")))
            self.default_return()
        if _input == 4:
            # # STRETCH - UPDATE existing order
            #
            #         PRINT orders list with its index values
            #         GET user input for order index value
            #         FOR EACH key-value pair in selected order:
            #             GET user input for updated property
            #             IF user input is blank:
            #                 do not update this property
            #             ELSE:
            #                 update the property value with user input
            print(tabulate(self.Orderdictlist, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))
            orderID = int(input("please input your order id to update: "))
            orderName = input("please input your new order name [default: press enter]: ") or "default"
            orderAddress = input("please input your new order Address [default: press enter]: ") or "default"
            orderPhoneNumber = input("please input your new order phoneNumber [default: press enter]: ") or "default"
            self.update_order_by_id(orderID, name=orderName, address=orderAddress, PhoneNumber=orderPhoneNumber)
            print(tabulate(self.Orderdictlist, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
            self.default_return()
        elif _input == 3:
            # STRETCH GOAL - UPDATE existing product
            # PRINT order names with its index value
            # GET user input for order index value
            # GET user input for new order name
            # UPDATE order name at index in products list
            print(tabulate(self.Orderdictlist, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))
            orderID = int(input("please input your order id to update: "))
            print(f"order \nid: type\n {json.dumps(self.orderTypes, indent=2, sort_keys=True)}")
            orderStatusID = int(input("please input your new order status id: "))
            self.update_order_status_by_id(orderID, orderStatusID)
            self.default_return()
        elif _input == 2:
            # Create Order
            # GET user input for customer name
            # GET user input for customer address
            # GET user input for customer phone number
            # SET order status to be 'PREPARING'
            # APPEND order to orders list
            self.create_order(input("please input your name: "), input("please input your address: "), input("please input your Phone Number: "))
            print(tabulate(self.Orderdictlist, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
            self.default_return()
        elif _input == 1:
            # PRINT products list
            print(tabulate(self.Orderdictlist, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
            self.default_return()
        elif _input == 0:
            # RETURN to main menu
            return 0

    def create_order(self, name, address, phoneNum):
        self.db.getDB()["orders"].append({"name": name, "address": address, "PhoneNumber": phoneNum, "status": self.orderTypes[1]})
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
        self.Orderdictlist.clear()
        self.kvdict = {}
        # print(self.dcm)
        for item in self.db.getDB()["orders"]:
            index = self.db.getDB()["orders"].index(item)
            index += 1
            self.kvdict[index] = item
            # print(f"Adding: k:{index}, v:{item}")
            self.Orderdictlist.append([item, index])

    def __repr__(self):
        return 0

    def default_return(self):
        self.recreate_list()
        print(tabulate(self.defaultlist, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
        self.open_menu(int(input("please input your order option: ") or "0"))
