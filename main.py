import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

data_menu = Menu()
make_coffee = CoffeeMaker()
pay_check = MoneyMachine()
items = data_menu.get_items()

while 1:
    user_input = str(input(f"What would you like? {items}: ")).lower()
    if user_input == "off":
        exit(0)
    elif user_input == "report":
        make_coffee.report()
        pay_check.report()
    elif data_menu.find_drink(user_input):
        drink = data_menu.find_drink(user_input)
        if make_coffee.is_resource_sufficient(drink) and pay_check.make_payment(drink.cost):
            make_coffee.make_coffee(drink)
    print("\n"*10)
