from art import logo
import os


print(logo)

bids = {}
end_of_bider = False


def find_highest_bidder(bidding_record):

    winner = ""
    highest_bidder = 0

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bidder}")

            # print(winner)


while not end_of_bider:
    name = input("What is your name?: ")
    price = input("What's your bid?: ")
    price = int(price)
    bids[name] = price

    add = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if add == "no":
        end_of_bider = True
        find_highest_bidder(bids)

    elif add == "yes":
        os.system("clear")

    print(bids)
