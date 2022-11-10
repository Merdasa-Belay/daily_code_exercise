from turtle import Screen
import time
# from turtle import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen .setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)


snake = Snake()

# snake.create_snake()
scoreboard = ScoreBoard()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

GAME_ON = True
while GAME_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        GAME_ON = False
        print("collision")

screen.exitonclick()
