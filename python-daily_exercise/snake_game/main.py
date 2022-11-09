from turtle import Screen, Turtle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
screen.title("Snake Game")
screen.tracer(0)
player_list = [(0, 0), (-20, 0), (-40, 0), ]


player_square = []
for cordx in player_list:
    player = Turtle()
    player.shape("square")
    player.color("white")
    player.penup()
    player.speed(1)
    player.goto(cordx)

    player_square.append(player)


def up():
    player_square[0].setheading(90)


def down():
    player_square[0].setheading(270)


def left():
    player_square[0].setheading(180)


def right():
    player_square[0].setheading(0)


screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

screen.listen()

GAME_ON = True
while GAME_ON:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(player_square) - 1, 0, -1):
        new_x = player_square[seg_num - 1].xcor()
        new_y = player_square[seg_num - 1].ycor()
        player_square[seg_num].goto(new_x, new_y)

    player_square[0].forward(20)


screen.exitonclick()
