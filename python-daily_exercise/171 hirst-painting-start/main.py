#! /usr/bin/env python3
### This code will not work in repl.it as there is no access to the colorgram package here.###
## We talk about this in the video tutorials##
import turtle as t
import colorgram
import random
eyob = t.Turtle()
eyob.shape("circle")
eyob.speed("fastest")
eyob.penup()
eyob.hideturtle()
t.colormode(255)
eyob.setheading(225)
eyob.forward(300)
eyob.setheading(0)

directions = [0, 90, 180, 270]


screen = t.Screen()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

for _ in range(0, 5):
    for _ in range(0, 10):
        eyob.setheading(0)
        eyob.forward(30)
        eyob.dot(20, random.choice(rgb_colors))

    eyob.setheading(90)
    eyob.forward(30)
    for _ in range(0, 10):
        eyob.dot(20, random.choice(rgb_colors))
        eyob.setheading(180)
        eyob.forward(30)
    eyob.setheading(90)
    eyob.forward(30)

screen.exitonclick()
