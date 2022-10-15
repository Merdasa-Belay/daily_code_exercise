import random
from hangman_art import stages
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.







display = []
for dash in range(len(chosen_word)):
  dash = "_"
  display += dash
print(display)





# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for letter in chosen_word:
#   if letter == guess:
#     print(guess)
#   else:
#     print("_")
live = 6

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(len(chosen_word)):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    live -= 1
    if live == 0:
      end_of_game = True
      print("You finished your life")

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")
  print(stages[live])

  
# for letter in chosen_word:
  


    #Step 2
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".


