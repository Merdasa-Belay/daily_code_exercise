#!/usr/bin/env python3

from turtle import Turtle, Screen


eyob = Turtle()

screen = Screen()

def move_forward():
    eyob.forward(30)


def move_backward():
  eyob.backward(30)

def move_counter_clockwise():
  eyob.right(90)
  
def move_clockwise():
  eyob.left(90)

def clear():
  eyob.clear()
  eyob.penup()
  eyob.home()
  eyob.pendown()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()