import time

from tabulate import tabulate

from Handlers.CouriersMenuHandler import CouriersMenuHandler
from Handlers.OrdersMenuHandler import OrdersMenuHandler
from Handlers.ProductMenuHandler import ProductMenuHandler
from utils.JsonDatabase import JsonDatabase


if __name__ == '__main__':
    # test database insert, select, update, delete
    database = JsonDatabase()

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
