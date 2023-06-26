#!/usr/bin/env python3
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
Menu = Menu()

is_machine_on = True
while is_machine_on:

    order = input(Menu.get_items())
    if order == "off":
        is_machine_on = False

    elif order == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(order)
        if CoffeeMaker.is_resource_sufficient(drink):
            if MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)
