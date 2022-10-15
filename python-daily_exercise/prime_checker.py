def prime_checker(number):
    no_factor = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            no_factor += str(divider)
    print(f"The factors for {number} is {no_factor}")
    length = len(no_factor)
    print(f"The number of factors are {length}")

    if length == 2:

        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
