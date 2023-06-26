#!/bin/python3
from art import logo
from game_data import data
from random import randint
from art import vs

print(logo)

length = len(data)

Compare_A = randint(0,length-1)


print(f"Compare A: {data[Compare_A]['name']}, a {data[Compare_A]['description']}, from {data[Compare_A]['country']}.")

print(vs)

compare_B = randint(0,length-1)
print(f"Compare B: {data[compare_B]['name']}, a {data[compare_B]['description']}, from {data[compare_B]['country']}.")

while True:
  
  answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
  if answer == 'A':
    if data[Compare_A]['follower_count'] > data[compare_B]['follower_count']:
      print(f"Compare A: {data[Compare_A]['name']} has {data[Compare_A]['follower_count']} million followers")
      print("You are right")
      print(f"Compare A: {data[Compare_A]['name']}, a {data[Compare_A]['description']}, from {data[Compare_A]['country']}.")
      print(vs)
      compare_B = randint(0,length-1)
      print(f"Compare B: {data[compare_B]['name']}, a {data[compare_B]['description']}, from {data[compare_B]['country']}.")
  elif answer == 'B':
      if data[Compare_A]['follower_count'] < data[compare_B]['follower_count']:
        print(f"Compare B: {data[compare_B]['name']} has {data[compare_B]['follower_count']} million followers")
        print("You are right")
        print(f"Compare A: {data[compare_B]['name']}, a {data[compare_B]['description']}, from {data[Compare_A]['country']}.")
        print(vs)
        compare_B = randint(0,length-1)
        print(f"Compare B: {data[compare_B]['name']}, a {data[compare_B]['description']}, from {data[compare_B]['country']}.")
        print(f"Compare B: {data[compare_B]['name']} has {data[compare_B]['follower_count']} million followers")
    
  else:
    print("Please enter a valid input")

