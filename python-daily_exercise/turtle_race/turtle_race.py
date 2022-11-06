from turtle import Turtle,  Screen
from random import randint
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="which turtle color will win the race:")


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


color_list = ["yellow", "red", "blue", "purple", "black", "brown", "orange"]
turtle_list = []
for n in range(0, 6):
    is_y_value = -150 + (n*50)
    user_turtle = Turtle()
    user_turtle.shape("turtle")
    user_turtle.color(color_list[n])
    user_turtle.penup()
    user_turtle.goto(x=-220, y=is_y_value)
    turtle_list.append(user_turtle)

if user_bet:
    GAME_ON = True

while GAME_ON:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You win!!! The winner color is {user_bet}")
            else:
                print(f"You lost!!! The winner  color is {winner_color}")
            GAME_ON = False
        is_random_forward = random.randint(0, 10)
        turtle.forward(is_random_forward)


screen.exitonclick()
