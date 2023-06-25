#!/usr/bin/env python3
from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

GAME_IS_ON = True


while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()


# TODO Detect collision with food.

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        food.refresh()


screen.exitonclick()
