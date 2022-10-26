from turtle import Turtle, Screen
from random import randint
import random

import turtle as turtle

t = turtle.Screen()

t = turtle.Turtle()
r = 100

m = turtle.Screen()
m.colormode(255)

# rich = Turtle()
t.speed(15)
t.width(5)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(angles):
    itrat = int(360 / angles)

    for _ in range(itrat):
        t.pencolor(random_color())
        t.circle(r)
        t.left(angles)
    return itrat


itrate = draw_spirograph(angles=10)


screen = Screen()

screen.exitonclick()
