from tabulate import tabulate

from utils.Logging import Logging


class Couriers:
    def __init__(self, db):
        self.DEBUG = False
        self.db = db
        self.CouriersDict = []
        self.logUtil = Logging("Couriers", False)

    def getCouriers(self):
        return self.CouriersDict

    def print_couriers(self):
        print(tabulate(self.CouriersDict, headers=['Courier Management Manu', 'Option Number'], tablefmt="outline"))

    def create_courier(self, name):
        self.db.getDB()["couriers"].append({
            "name": name,
            "created_at": self.logUtil.timestamp()
        })
        self.db.writeFile()
        self.regenerate_couriers()

    def update_courier_by_id(self, index, **kwargs):
        for key, value in kwargs.items():
            if not value == "default":
                self.db.getDB()["couriers"][index - 1].update({f"{key}": value})
        self.db.getDB()["couriers"][index - 1].update({"updated_at": self.logUtil.timestamp()})
        self.db.writeFile()
        self.regenerate_couriers()

    def remove_from_db(self, index):
        if self.check_within_range(self.db.getDB()['couriers'], index):
            print(f"index: {index - 1}, removedItem: {self.db.getDB()['couriers'][index - 1]}")
            self.db.getDB()["couriers"].pop(index - 1)
            self.db.writeFile()
            self.regenerate_couriers()
        else:
            print(f"please use a value between [1 and {self.db.getDB()['couriers'].__len__()}]")

    def regenerate_couriers(self):
        self.CouriersDict.clear()
        # print(self.dcm)
        for item in self.db.getDB()["couriers"]:
            index = self.db.getDB()["couriers"].index(item)
            index = self.db.getDB()["couriers"].index(item)
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
