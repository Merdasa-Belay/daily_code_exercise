import turtle as t
import random


eyob = t.Turtle()
t.colormode(255)

color = ["red", "blue", "yellow", "black", "green"]
directions = [0, 90, 180, 270]
eyob.shape("circle")


# eyob.penup()
eyob.pensize(15)

eyob.speed("fastest")

GAME_ON = True

while GAME_ON:

    eyob.color(random.choice(color))
    eyob.forward(20)
    eyob.setheading(random.choice(directions))


screen = t.Screen()

screen.exitonclick()