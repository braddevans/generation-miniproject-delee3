import json
import os
import sys

databaseFile = "database.json"


class JsonDatabase:
    def __init__(self):
        self.db = {
            "products": [],
            "orders": [],
            "couriers": []
        }

        if self.checkExists(databaseFile):
            self.readFile()
        else:
            self.init()
            self.writeFile()
            self.readFile()


    def write_path(self, path, value):
        # string split
        curr = {}
        for key in path:
            if key not in curr:
                curr[key] = {}
            curr = curr[key]
        k, v = value
        curr[k] = v
        self.db.update(curr)
        self.writeFile()

    def getDB(self):
        return self.db

    def init(self):
        self.write_path(["data"],
                        ("products",
                         ["7 Up", "50/50", "A&W Cream Soda", "Canada Dry", "Canfield's Diet Chocolate Fudge", "Cheerwine", "Coca-Cola", "Coca-Cola Black Cherry Vanilla", "Coca-Cola BlāK", "Coca-Cola C2", "Coca-Cola Cherry",
                          "Coca-Cola Citra", "Coca-Cola Clear", "Coca-Cola Life", "Coca-Cola Light", "Coca-Cola Light Sango", "Coca-Cola Orange", "Coca-Cola Orange Vanilla", "Coca-Cola Raspberry", "Coca-Cola Vanilla", "Coca-Cola Zero",
                          "Coca-Cola with Lemon", "Coca-Cola with Lime", "Cream Soda", "Crush", "Crystal Pepsi", "Dasani", "Delaware Punch", "Diet Coke", "Diet Coke Lime", "Diet Coke Plus", "Diet Coke with Citrus Zest", "Diet Coke with Lemon",
                          "Diet Coke with Zesty Blood Orange", "Diet Inca Kola", "Diet Mountain Dew", "Diet Pepsi", "Diet Rite", "Dr Brown's", "Dr Pepper", "Duke's", "Fanta", "Fanta Citrus", "Fanta Exotic", "Fantasy", "Faygo", "Fayrouz", "Floats",
                          "Fresca", "Frescolihi", "Frescolita", "Full Throttle", "Gatorade", "Gini", "Grape", "Hamoud", "Hamoud Boualem", "Hawaiian Punch", "Hires Root Beer", "IBC Root Beer", "Inca Kola", "Irn-Bru", "Jarritos", "Jones Soda",
                          "Julmust", "Keurig Dr Pepper", "KickStart"]))

    def checkExists(self, file):
        return os.path.exists(os.getcwd() + os.sep + file)

    def readFile(self):
        with open(databaseFile) as database_file:
            self.db = json.load(database_file)

    def writeFile(self):
        with open(databaseFile, "w") as outfile:
            outfile.write(json.dumps(self.db, indent=2, sort_keys=True))

        self.readFile()
