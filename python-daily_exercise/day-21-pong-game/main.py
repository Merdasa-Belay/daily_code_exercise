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

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
GAME_IS_ON = True
while GAME_IS_ON:
    screen.update()
screen.exitonclick()
