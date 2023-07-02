#!/usr/bin/env python3
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
ball = Ball()
score_board = Scoreboard()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # TODO Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO Detecting collision with r_paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO Detect when r_paddle misses

    if ball.xcor() > 380:
        ball.refresh()
        score_board.l_point()

    # TODO Detect when l_paddle misses

    if ball.xcor() < -380:
        ball.refresh()
        score_board.r_point()


screen.exitonclick()
