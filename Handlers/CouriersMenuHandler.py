import json

from tabulate import tabulate

from Objects.Couriers import Couriers


class CouriersMenuHandler:
    def __init__(self, dcm):
        self.db = dcm
        self.defaultlist = [
            ['Return to Main Menu', 0],
            ['PRINT courier list', 1],
            ['CREATE new courier', 2],
            ['UPDATE existing courier', 3],
            ['DELETE courier', 4]
        ]
        # create courier handler class passing in the json database
        self.couriers = Couriers(self.db)

        print(tabulate(self.defaultlist, headers=['Courier Management Manu', 'Option Number'], tablefmt="outline"))

        self.open_menu(int(input("please input your courier option: ") or "0"))

    def open_menu(self, _input):
        # regenerate the self.CouriersDict using the below function to get the new values from the database file
        self.couriers.regenerate_couriers()

        if _input == 4:
            # STRETCH GOAL - DELETE courier
            self.couriers.print_couriers()
            self.couriers.remove_from_db(int(input("please input your courier you want to delete: ")))
            self.default_return()

        if _input == 3:
            # # STRETCH - UPDATE existing courier
            self.couriers.print_couriers()

            # take user input into variables but use a default return of "default" if the user doesn't input anything
            courier_id = int(input("please input your courier id to update: "))
            courier_name = input("please input your new courier name [default: press enter]: ") or "default"

            # update the courier using the above input variables taken from the user into a kwargs dict to be looped over in the next function
            self.couriers.update_courier_by_id(courier_id, name=courier_name)
            self.couriers.print_couriers()
            self.default_return()

        elif _input == 2:
            # Create Courier
            self.couriers.create_courier(input("please input your name: "))
            self.couriers.print_couriers()
            self.default_return()

        elif _input == 1:
            # PRINT courier list
            self.couriers.print_couriers()
            self.default_return()

        elif _input == 0:
            # RETURN to main menu
            return 0

    def __repr__(self):
        return 0

    def default_return(self):
        print(tabulate(self.defaultlist, headers=['Courier Management Manu', 'courier Number'], tablefmt="outline"))
        self.open_menu(int(input("please input your courier option: ") or "0"))
