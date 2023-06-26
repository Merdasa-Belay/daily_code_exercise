#!/usr/bin/env python3
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
ball = Ball()

paddle = Paddle()
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
GAME_IS_ON = True
while GAME_IS_ON:
  screen.update()

screen.exitonclick()