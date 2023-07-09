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


# TODO-1 Detect collision with food.

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        food.refresh()
        snake.extend()
# TODO-2 Detect collision with the food
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
# TODO- 3 Detect collision with tail
    for seg in snake.snake_index[1:]:

        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
