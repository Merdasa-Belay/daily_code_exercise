from art import vs
from game_data import data
from art import logo
# from replit import clear
import os

import random

print(logo)

end_game = False


def select_randomly(data):
    is_compare_data = random.choice(data)

    return is_compare_data


def is_sliced_followers(compare_data):
    is_compare_count = compare_data['follower_count']
    is_compare_name = compare_data['name']
    return is_compare_count, is_compare_name


def return_letter(letter_1, letter_2):

    return "a" if letter_1[0] > letter_2[0] else "b"


def find_highest_follower(data_1, data_2):
    """find_highest_follower function returns highest number"""

    highest_follower = 0

    if data_1[0] > data_2[0]:

        highest_follower = data_1
        return highest_follower

    if data_2[0] > data_1[0]:
        highest_follower = data_2
        return highest_follower
    # if data_2[0] == data_1[0]:
    #   highest_follower =


compare_data_1 = select_randomly(data)
followers_1 = is_sliced_followers(compare_data_1)
print(followers_1[1])
print(vs)

guess = ""
score = 0

highest_follower_next = followers_1
while not end_game:
    compare_data_new = select_randomly(data)
    compare_new_followers = is_sliced_followers(compare_data_new)
    while compare_new_followers == highest_follower_next:
        compare_data_new = select_randomly(data)
        compare_new_followers = is_sliced_followers(compare_data_new)
    print(compare_new_followers[1])
    highest_follower_next = find_highest_follower(highest_follower_next,
                                                  compare_new_followers)
    print(highest_follower_next)
    returned_letter_next = return_letter(letter_1=highest_follower_next,
                                         letter_2=compare_new_followers)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == returned_letter_next:

        # clear()
        os.system('clear')
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}.")
        print(highest_follower_next[1])
        print(vs)
    elif guess != returned_letter_next:
        print(f"Sorry, that's wrong. Final score: {score}")

        end_game = True
