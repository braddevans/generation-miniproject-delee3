from tabulate import tabulate

from utils.Logging import Logging


class Couriers:
    def __init__(self, db):
        self.DEBUG = False
        self.database = db
        self.CouriersDict = []
        self.logUtil = Logging("Couriers", False)
        self.regenerate_couriers()

    def getCouriers(self):
        return self.CouriersDict

    def print_couriers(self):
        print(tabulate(self.CouriersDict, headers=['Courier Management Manu', 'Option Number'], tablefmt="outline"))

    def create_courier(self, name):
        self.database.getDB()["couriers"].append({
            "name": name
        })
        self.database.writeFile()

        self.regenerate_couriers()

    def update_courier_by_id(self, index, **kwargs):
        for key, value in kwargs.items():
            if not value == "default":
                self.database.getDB()["couriers"][index - 1].update({f"{key}": value})
        self.database.writeFile()

        self.regenerate_couriers()

    def remove_from_db(self, index):
        if self.check_within_range(self.database.getDB()['couriers'], index):
            print(f"index: {index - 1}, removedItem: {self.database.getDB()['couriers'][index - 1]}")
            self.database.getDB()["couriers"].pop(index - 1)
            self.database.writeFile()

            self.regenerate_couriers()
        else:
            print(f"please use a value between [1 and {self.database.getDB()['couriers'].__len__()}]")

    def get_courier_by_id(self, courier_id):
        return self.database.getDB()["couriers"][courier_id]

    def regenerate_couriers(self):
        self.CouriersDict.clear()
        # print(self.dcm)
        for item in self.database.getDB()["couriers"]:
            index = self.database.getDB()["couriers"].index(item)
            index += 1
            self.CouriersDict.append([item, index])

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
