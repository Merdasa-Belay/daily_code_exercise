import os
from art import logo

print(logo)

end_operation = False


def add(num1, num2):
    ans = num1 + num2
    return ans


def subtract(num1, num2):
    ans = num1 - num2
    return ans


def multiply(num1, num2):
    ans = num1 * num2
    return ans


def divide(num1, num2):
    ans = num1 / num2
    return ans


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

# def operations(num1, num2):

#     if operation == "+":
#         ans = add(num1, num2)
#         print(ans)

#     elif operation == "-":
#         ans = subtract(num1, num2)
#         print(ans)

#     elif operation == "*":
#         ans = multiply(num1, num2)
#         print(ans)

#     elif operation == "/":
#         ans = divide(num1, num2)
#         print(ans)
# else:

# print("Invaid operator")
# end_of_operation = False


def calculator():
    num1 = float(input("What is the first number: "))

    while not end_operation:

        #     operation = input("""
        #     Pick an operation:
        #     +
        #     *
        #     /
        #     -
        #     """)

        num2 = float(input("What is the next number: "))
        for operator in operation:
            print(operator)
        operator = input("Pick an operation: ")

        calculation_function = operation[operator]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator} {num2} = {calculation_function(num1, num2)}")
        want_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to new start a new calculation: "
        )

        if want_continue == "n":
            os.system('clear')
            calculator()

        elif want_continue == "y":
            num1 = answer
            calculation_function(num1, num2)


calculator()
