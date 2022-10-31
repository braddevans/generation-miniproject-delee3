from tabulate import tabulate


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
        self.ProductList = []

        print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
        self.open_menu(int(input("please input your product option: ")))

    #
    # menu loop
    #
    def open_menu(self, _input):
        self.recreate_list()
        if _input == 4:
            # STRETCH GOAL - DELETE product
            # PRINT products list
            # GET user input for product index value
            # DELETE product at index in products list
            print(tabulate(self.ProductList, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.remove_from_list(int(input("please input your product you want to delete: ")))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))

        elif _input == 3:
            # STRETCH GOAL - UPDATE existing product
            # PRINT product names with its index value
            # GET user input for product index value
            # GET user input for new product name
            # UPDATE product name at index in products list
            print(tabulate(self.ProductList, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.update_list(int(input("please input your updated product id: ")), input("please input your updated product name: "))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))

        elif _input == 2:
            # CREATE new product
            # GET user input for product name
            # APPEND product name to products list
            self.add_to_list(input("please input your product name: "))
            print(tabulate(self.ProductList, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))

        elif _input == 1:
            # PRINT products list
            print(tabulate(self.ProductList, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))

        elif _input == 0:
            # RETURN to main menu [goto __repr__()]
            return 0

    #
    # functions
    #

    def add_to_list(self, item):
        self.db.getDB()["products"].append(item)
        self.db.writeFile()
        self.recreate_list()
        pass

    def update_list(self, index, item):
        self.db.getDB()["products"][index - 1] = item
        self.db.writeFile()
        self.recreate_list()
        pass

    def remove_from_list(self, index):
        print(f"index: {index - 1}, removedItem: {self.db.getDB()['products'][index - 1]}")
        self.db.getDB()["products"].pop(index - 1)
        self.db.writeFile()
        self.recreate_list()
        pass

    def recreate_list(self):
        self.ProductList.clear()
        # print(self.dcm)
        for item in self.db.getDB()["products"]:
            index = self.db.getDB()["products"].index(item)
            index += 1
            self.ProductList.append([item, index])

    # return pointer for class
    def __repr__(self):
        return 0
