import csv

from tabulate import tabulate

from Objects.Couriers import Couriers
from Objects.Order import Order
from Objects.Product import Product


class CSVIOHandler:
    def __init__(self, dcm):
        self.db = dcm
        self.defaultlist = [
            ['Return to Main Menu', 0],
            ['IMPORT CSV', 1],
            ['EXPORT CSV', 2]
        ]
        self.products = Product(self.db)
        self.orders = Order(self.db)
        self.couriers = Couriers(self.db)

        self.courier_headers = ["id", "name"]
        self.order_headers = ["id", "name", "address", "phone", "created_at", "items", "courier", "status"]
        self.product_headers = ["id", "name", "price"]

        self.courier_list = []
        self.order_list = []
        self.product_list = []

        self.default_return()

    #
    # menu loop
    #
    def open_menu(self, _input):
        if _input == 2:
            # Export
            print(f"couriers: {len(self.couriers.getCouriers())}")
            for i in range(len(self.couriers.getCouriers())):
                self.courier_list.append([self.couriers.get_courier_by_id(i).name])
                print(self.couriers.get_courier_by_id(i))
            self.csv_write("couriers.csv", self.courier_headers, self.courier_list)

            print(f"orders: {len(self.orders.getOrders())}")
            for i in range(len(self.orders.getOrders())):
                order = self.orders.get_order_by_id(i)
                print(order)
                self.order_list.append(
                    [
                        order["customer_name"],
                        order["customer_address"],
                        order["customer_phone"],
                        order["created_at"],
                        order["items"],
                        order["courier"],
                        order["status"]
                    ]
                )
            self.csv_write("orders.csv", self.order_headers, self.order_list)

            print(f"products: {len(self.products.getProducts())}")
            for i in range(len(self.products.getProducts())):
                product = self.products.get_product_by_id(i)
                print(product)
                self.product_list.append(
                    [
                        product["name"],
                        product["price"]
                    ]
                )
            self.csv_write("products.csv", self.product_headers, self.product_list)

            self.db.writeFile()

            self.default_return()

        elif _input == 1:
            # Import
            should_fully_regen_db = bool(input("Should Delete All old values [if ⏎, will be left unchanged] (True, False):") or False)
            if should_fully_regen_db:
                for i in range(len(self.couriers.getCouriers())):
                    self.couriers.remove_from_db(i)
                for i in range(len(self.orders.getOrders())):
                    self.orders.remove_from_db(i)
                for i in range(len(self.products.getProducts())):
                    self.products.remove_from_db(i)

            self.db.writeFile()

            self.default_return()

        elif _input == 0:
            # RETURN to main menu [goto __repr__()]
            return 0

    def csv_write(self, csv_filename, headers, data):
        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            # create the csv writer
            writer = csv.writer(f)
            writer.writerow(headers)

            # write a row to the csv file
            index = 0
            for row in data:
                row_list = [index]
                for i in row:
                    row_list.append(i)
                writer.writerow(row_list)
                index += 1

    def default_return(self):
        print(tabulate(self.defaultlist, headers=['Management Manu', 'Choice'], tablefmt="outline"))
        self.open_menu(int(input("please input your option: ") or "0"))

    def __repr__(self):
        return 0
