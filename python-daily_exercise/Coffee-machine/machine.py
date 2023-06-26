#!/usr/bin/env python3
from main import MENU
from main import resources

# TODO 1. Print report of all coffee machine resources


def report():
    """reporting resources"""
    for resource in resources:
        print(f"{resource}: {resources[resource]}")

   # TODO 2. Check resources sufficient to make drink order


def check_resources():
    """checking resources"""
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        print("Please insert coins.")
    elif resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
        print("Please insert coins.")
    elif resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
        print("Please insert coins.")
    else:
        print("Sorry, there is not enough resources.")
# TODO 3. update resources


def update_resources():
    """updating resources"""
    if order == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif order == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    elif order == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]

# TODO 4. Process coins


def process_coins():
    """Returns the total calculated from coins inserted."""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def check_transaction(total):

    if MENU["espresso"]["cost"] <= total:
        print(
            f"Here is ${round(total - MENU['espresso']['cost'], 2)} in change.")
        print("Here is your espresso ☕. Enjoy!")
    elif MENU["latte"]["cost"] <= total:
        print(f"Here is ${round(total - MENU['latte']['cost'], 2)} in change.")
        print("Here is your latte ☕. Enjoy!")
    elif MENU["cappuccino"]["cost"] <= total:
        print(
            f"Here is ${round(total - MENU['cappuccino']['cost'], 2)} in change.")
        print("Here is your cappuccino ☕. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")


MACHINE = True

while MACHINE:

    order = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    update_resources()

    if order == "report":
        report()
    elif order == "espresso":
        check_resources()

        check_transaction(total=process_coins())

    elif order == "latte":
        check_resources()
        check_transaction(total=process_coins())

    elif order == "cappuccino":
        check_resources()
        check_transaction(total=process_coins())

    elif order == "off":
        MACHINE = False
    else:
        print("Please enter a valid order")
        order = input("What would you like? (espresso/latte/cappuccino): ")
