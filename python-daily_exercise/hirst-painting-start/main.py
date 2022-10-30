from turtle import Turtle, Screen
import turtle
from random import randint
import random


t = turtle.Screen()
t.colormode(255)
eyob = Turtle()


###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# # print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb = (r, g, b)

#     rgb_colors.append(new_rgb)
# print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145,
                                                                                                                                                                                                             178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
directions = [0, 90, 180, 270]
eyob.shape("arrow")
eyob.speed('fastest')
number_of_dots = 0
eyob.penup()
eyob.hideturtle()
for i in range(10):
    eyob.goto(0, number_of_dots)
    for j in range(10):
        eyob.dot(20, random.choice(color_list))
        eyob.forward(50)
    number_of_dots += 50


screen = t.Screen()
screen.screensize(400, 300)
screen.exitonclick()
