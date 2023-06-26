from turtle import Turtle, Screen

import random

colors = ["red", "blue", "yellow", "brown", "green"]


eyob = Turtle()


eyob.shape("turtle")


GAME_ON = True

n = 3

while GAME_ON:


  for _ in range(n):
    eyob.forward(100)
    eyob.right(360/n)
    eyob.color(random.choice(colors))

  n += 1





screen = Screen()



screen.exitonclick()