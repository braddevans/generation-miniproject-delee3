import json

from tabulate import tabulate

from Objects.Order import Order


class OrdersMenuHandler:
    def __init__(self, dcm):
        self.db = dcm
        self.defaultlist = [
            ['Return to Main Menu', 0],
            ['PRINT orders list', 1],
            ['CREATE new order', 2],
            ['UPDATE existing order status', 3],
            ['UPDATE existing order', 4],
            ['DELETE order', 5]
        ]
        # create order handler class passing in the json database
        self.orders = Order(self.db)

        print(tabulate(self.defaultlist, headers=['Order Management Manu', 'Option Number'], tablefmt="outline"))

        self.open_menu(int(input("please input your order option: ") or "0"))

    def open_menu(self, _input):
        # regenerate the self.OrderDict using the below function to get the new values from the database file
        self.orders.regenerate_orders()

        if _input == 5:
            # STRETCH GOAL - DELETE order
            self.orders.print_orders()
            self.orders.remove_from_db(int(input("please input your order you want to delete: ")))
            self.default_return()

        if _input == 4:
            # # STRETCH - UPDATE existing order
            self.orders.print_orders()

            # take user input into variables but use a default return of "default" if the user doesn't input anything
            order_id = int(input("please input your order id to update: "))
            order_name = input("please input your new order name [default: press enter]: ") or "default"
            order_address = input("please input your new order Address [default: press enter]: ") or "default"
            order_phone_number = input("please input your new order phoneNumber [default: press enter]: ") or "default"

            # update the order using the above input variables taken from the user into a kwargs dict to be looped over in the next function
            self.orders.update_order_by_id(order_id, name=order_name, address=order_address, PhoneNumber=order_phone_number)
            self.orders.print_orders()
            self.default_return()

        elif _input == 3:
            # STRETCH GOAL - UPDATE existing product
            self.orders.print_orders()

            order_id = int(input("please input your order id to update: "))

            print(f"order \nid: type\n {json.dumps(self.orders.getTypes(), indent=2, sort_keys=True)}")
            order_status_id = int(input("please input your new order status id: "))
            self.orders.update_order_status_by_id(order_id, order_status_id)
            self.default_return()

        elif _input == 2:
            # Create Order
            self.orders.create_order(input("please input your name: "), input("please input your address: "),
                                     input("please input your Phone Number: "))
            self.orders.print_orders()
            self.default_return()

        elif _input == 1:
            # PRINT products list
            self.orders.print_orders()
            self.default_return()

        elif _input == 0:
            # RETURN to main menu
            return 0

    def __repr__(self):
        return 0

    def default_return(self):
        print(tabulate(self.defaultlist, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
        self.open_menu(int(input("please input your order option: ") or "0"))
