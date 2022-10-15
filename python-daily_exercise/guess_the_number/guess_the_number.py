from art import logo
import random

# end_game = False

print(logo * 3)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
card = list(range(1, 101))
# print(card)

rand_num = random.choice(card)

print(f"Pssst, the correct answer is {rand_num}")
player_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
computer_card = random.choice(card)
# print(computer_card)


def difficulty_choice(player_choice):
    if player_choice == "hard":
        return 5

    elif player_choice == "easy":
        return 10


attempt = difficulty_choice(player_choice)
# print(attempt)


def game():
    def guess_checker(attempt):
        # end_game = False
        while attempt > 0:

            guess = int(input("Make a guess: "))
            attempt -= 1

            def attempt_checker(attempt):
                if attempt == 0:
                    print("You've run out of guesses, you lose.")
                    # attempt = False
                else:
                    print(
                        f"You have {attempt} attempts remaining to guess the number.")

            if guess < computer_card:
                print("Too low.")
                print("Guess again")
                # return attempt

            elif guess > computer_card:
                print("Too high.")
                print("Guess again.")

                # attempt_checker(attempt)

            elif guess == computer_card:
                print(f"You got it! The answer was {guess}.")

                # end_game = True
                return
                # attempt_checker(attempt)

            attempt_checker(attempt)

    guess_checker(attempt)


game()
