from random import randint

from tabulate import tabulate

from Objects.Product import Product


class ProductMenuHandler:
    def __init__(self, dcm):
        self.db = dcm
        self.defaultlist = [
            ['Return to Main Menu', 0],
            ['PRINT products list', 1],
            ['CREATE new product', 2],
            ['UPDATE existing product', 3],
            ['DELETE product', 4]
        ]
        self.products = Product(self.db)
        self.default_return()

    #
    # menu loop
    #
    def open_menu(self, _input):
        self.products.regenerate_products()
        if _input == 4:
            # STRETCH GOAL - DELETE product
            # PRINT products list
            # GET user input for product index value
            # DELETE product at index in products list

            self.products.print_products()

            product_id = int(input("please input your product id: "))

            self.products.remove_from_db(product_id)
            self.default_return()
            self.default_return()

        elif _input == 3:
            # STRETCH GOAL - UPDATE existing product
            # PRINT product names with its index value
            # GET user input for product index value
            # GET user input for new product name
            # UPDATE product name at index in products list

            self.products.print_products()

            # take user input
            product_id = int(input("please input your product id [if ⏎, will be left unchanged]: "))
            product_name = int(input("please input your product name [if ⏎, will be left unchanged]: "))
            product_price = int(input("please input your product price [if ⏎, will be left unchanged]: "))

            self.products.update_product_by_id(product_id, name=product_name, price=product_price)
            self.default_return()

        elif _input == 2:
            # CREATE new product
            # GET user input for product name
            # APPEND product name to products list
            self.products.create_product(input("please input your product name: "), float(input("please input your product price: ") or "0"))
            self.products.print_products()
            self.default_return()

        elif _input == 1:
            # PRINT products list
            self.products.print_products()
            self.default_return()

        elif _input == 0:
            # RETURN to main menu [goto __repr__()]
            return 0

    def default_return(self):
        print(tabulate(self.defaultlist, headers=['Order Management Manu', 'Order Number'], tablefmt="outline"))
        self.open_menu(int(input("please input your order option: ") or "0"))

    def __repr__(self):
        return 0