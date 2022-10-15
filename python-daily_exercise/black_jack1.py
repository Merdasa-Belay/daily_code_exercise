############### Blackjack Project #####################

import random

end_of_game = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal_card(cards):
    random_choice = random.sample(cards, 2)
    return random_choice


def append(card_list, added):
    # first, second = cards
    card_list.append(added)

    # sum_list = sum(card_list)
    return card_list


user_cards = deal_card(cards)
print(user_cards)

computer_cards = deal_card(cards)
print(computer_cards)


def calculate_score(rand_choice):

    ace = 11
    summation = 0
    for number in rand_choice:
        summation += number
    # print(summation)
    if summation > 21:
        if ace in rand_choice:
            rand_choice.remove(11)
            rand_choice.append(1)
            return rand_choice
        elif ace not in rand_choice:
            return rand_choice

    elif summation == 21:
        # print("BlackJack")
        return 0
    else:
        return rand_choice


def sum_list(random_cards):
    if random_cards == 0:
        # print("Black_jack")
        return 0
    else:
        random_sum = 0
        for numbers in random_cards:
            random_sum += numbers
        return random_sum


user_list = calculate_score(rand_choice=user_cards)
# print(user_list)
user_sum = sum_list(random_cards=user_list)
print(user_sum)
computer_list = calculate_score(rand_choice=computer_cards)
computer_sum = sum_list(random_cards=computer_list)
print(computer_sum)



want_to_continue = input("Type 'y' to get another card type 'n' to push: ")


def add_list(add_list):
    random_choice = random.choice(cards)
    add_list.append(random_choice)
    sum_number = sum_list(add_list)
    return sum_number


if want_to_continue == 'y':
    user_added_list = add_list(add_list=user_list)
    print(user_added_list)
elif want_to_continue == 'n':
    end_of_game = True

