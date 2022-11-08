import time
from random import randint

from tabulate import tabulate

from Handlers.CouriersMenuHandler import CouriersMenuHandler
from Handlers.OrdersMenuHandler import OrdersMenuHandler
from Handlers.ProductMenuHandler import ProductMenuHandler
from Objects.Product import Product
from utils.JsonDatabase import JsonDatabase


def gen_initial_db():
    prod_list = [
        "7 Up", "50/50", "A&W Cream Soda", "Canada Dry", "Canfield's Diet Chocolate Fudge", "Cheerwine", "Coca-Cola",
        "Coca-Cola Black Cherry Vanilla", "Coca-Cola Orange", "Coca-Cola Zero", "Coca-Cola with Lime",
        "Coca-Cola Orange Vanilla", "Coca-Cola Raspberry", "Coca-Cola Vanilla",
        "Coca-Cola with Lemon"
    ]
    for item in prod_list:
        random_price = (randint(10, 100) / 100)
        products.create_product(item, random_price)
    database.writeFile()
    database.readFile()


if __name__ == '__main__':
    # test database insert, select, update, delete
    database = JsonDatabase()
    products = Product(database)

    if products.ProductDict.__len__() < 1:
        gen_initial_db()

    will_exit = False
    menu = tabulate([
        ['Product Management', 1],
        ['Orders Management', 2],
        ['Courier Management', 3],
        ['exit', 0]
    ], headers=['Menu Options', 'Option Number'], tablefmt="outline")

    while not will_exit:
        time.sleep(0.005)
        print(menu)
        userinput = int(input("please input your option: "))
        if userinput == 0:
            will_exit = True
        elif userinput == 1:
            userinput = ProductMenuHandler(database)
        elif userinput == 2:
            userinput = OrdersMenuHandler(database)
        elif userinput == 3:
            userinput = CouriersMenuHandler(database)
        else:
            userinput = int(input("please input your option: "))

        pass
