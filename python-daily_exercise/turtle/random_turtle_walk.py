from turtle import Turtle, Screen
import turtle
from random import randint
import random

eyob = Turtle()
t = turtle.Screen()
t.colormode(255)


def random_color():
    """random_color selects random colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


eyob.turtlesize(3)
eyob.width(10)
eyob.speed("fastest")

directions = [0, 90, 180, 270]
for _ in range(2000):
    eyob.forward(30)
    eyob.pencolor(random_color())

    eyob.setheading(random.choice(directions))


screen = Screen()
screen.screensize(400, 300)
screen.exitonclick()
