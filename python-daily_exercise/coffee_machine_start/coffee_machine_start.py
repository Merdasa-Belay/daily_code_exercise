from coffee_machine_data import MENU, resources


is_espresso = MENU['espresso']
is_latte = MENU['latte']
is_cappuccino = MENU['cappuccino']


espresso = is_espresso['ingredients']
espresso_cost = is_espresso['cost']
latte = is_latte['ingredients']
latte_cost = is_latte['cost']
cappuccino = is_cappuccino['ingredients']
cappuccino_cost = is_cappuccino['cost']

quarter_c = 0.25
dimes_c = 0.10
nickles_c = 0.05
pennies_c = 0.01

# print(resources)


def resource_calculator(resources_needed, order_ingredient):

    if resources_needed['coffee'] > order_ingredient['coffee']:
        resources_needed['water'] = resources_needed['water'] - \
            order_ingredient['water']
        resources_needed['milk'] = resources_needed['milk'] - \
            order_ingredient['milk']
        resources_needed['coffee'] = resources_needed['coffee'] - \
            order_ingredient['coffee']

    return resources_needed


def resource_calculator_espresso(resources_needed, order_ingredient):
    if resources_needed['water'] > order_ingredient['water']:
        if resources_needed['coffee'] > order_ingredient['coffee']:
            resources_needed['water'] = resources_needed['water'] - \
                order_ingredient['water']
            resources_needed['coffee'] = resources_needed['coffee'] - \
                order_ingredient['coffee']
            return resources_needed

        else:
            return f"Sorry there is not enough coffee."

    else:
        return f"Sorry there is not enough water."


def report(per_income, new_resources):

    print(f"water: {new_resources['water']}")

    print(f"Milk: {new_resources['milk']}")

    print(f"coffee: {new_resources['coffee']}")
    print(f"cost: ${per_income}")


def is_coin_sum(quarter, dimes, nickles, pennies):

    coin_sum = quarter + dimes + nickles + pennies
    return coin_sum


def coin_calculator(quarter, dimes, nickles, pennies):

    coin_sum = quarter_c * quarter + dimes_c * \
        dimes + nickles_c * nickles + pennies_c * pennies

    return coin_sum


end_game = True

income = 0
while end_game:
    order = (input("What would you like? (espresso/latte/cappuccino): "))
    if order == "report":

        report(per_income=income, new_resources=resources)

    if order == "latte":

        if resources['water'] > latte['water']:
            if resources['water'] > latte['milk']:
                if resources['water'] > latte['coffee']:
                    print("Please insert coins.")
                    is_quarter = float(input("how many quarters?: "))

                    is_dimes = float(input("how many dimes?: "))

                    is_nickles = float(input("how many nickles?: "))

                    is_pennies = float(input("how many pennies?: "))
                    money_sums = coin_calculator(
                        is_quarter, is_dimes, is_nickles, is_pennies)

                    resources = resource_calculator(
                        resources_needed=resources, order_ingredient=latte)
                    if money_sums > latte_cost:
                        change = money_sums - latte_cost
                        income += latte_cost
                        print(f"Here is ${change:.2f} in change.")
                        print("Here is your latte ☕️. Enjoy!")
                        # print(resources)
                    elif money_sums == latte_cost:
                        income += latte_cost
                        print("Here is your latte ☕️. Enjoy!")
                        # print(resources)
                    else:
                        print("Sorry there is not enough water.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough coffee.")

    elif order == "espresso":
        if resources['water'] > espresso['water']:
            if resources['water'] > espresso['coffee']:
                print("Please insert coins.")
                is_quarter = float(input("how many quarters?: "))

                is_dimes = float(input("how many dimes?: "))

                is_nickles = float(input("how many nickles?: "))

                is_pennies = float(input("how many pennies?: "))
                money_sums = coin_calculator(
                    is_quarter, is_dimes, is_nickles, is_pennies)

                resources = resource_calculator_espresso(
                    resources_needed=resources, order_ingredient=espresso)
                if money_sums > espresso_cost:
                    change = money_sums - espresso_cost
                    income += espresso_cost
                    print(f"Here is ${change:.2f} in change.")
                    print("Here is your espresso ☕️. Enjoy!")
                    # print(resources)
                elif money_sums == espresso_cost:
                    income += espresso_cost
                    print("Here is your espresso ☕️. Enjoy!")
                    # print(resources)
                else:
                    print("Sorry there is not enough water.")

        else:
            print("Sorry there is not enough coffee.")

    elif order == "cappuccino":
        if resources['water'] > cappuccino['water']:
            if resources['water'] > cappuccino['milk']:
                if resources['water'] > cappuccino['coffee']:
                    print("Please insert coins.")
                    is_quarter = float(input("how many quarters?: "))

                    is_dimes = float(input("how many dimes?: "))

                    is_nickles = float(input("how many nickles?: "))

                    is_pennies = float(input("how many pennies?: "))
                    money_sums = coin_calculator(
                        is_quarter, is_dimes, is_nickles, is_pennies)

                    resources = resource_calculator(
                        resources_needed=resources, order_ingredient=latte)
                    if money_sums > cappuccino_cost:
                        change = money_sums - cappuccino_cost
                        income += cappuccino_cost
                        print(f"Here is ${change:.2f} in change.")
                        print("Here is your cappuccino ☕️. Enjoy!")
                        # print(resources)
                    elif money_sums == cappuccino_cost:
                        income += cappuccino_cost
                        print("Here is your cappuccino ☕️. Enjoy!")
                        # print(resources)
                    else:
                        print("Sorry there is not enough water.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough coffee.")
