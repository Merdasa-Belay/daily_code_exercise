from turtle import Turtle, Screen
import time
from turtle import *

screen = Screen()
screen .setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
START = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)

segments = []
for position in START:
    segment = Turtle()
    segment.penup()
    segment.shape("square")
    segment.color("white")
    # screen.delay(100)
    segment.goto(position)
    segments.append(segment)


def up():
    segments[0].setheading(90)


def down():
    segments[0].setheading(270)


def left():
    segments[0].setheading(180)


def right():
    segments[0].setheading(0)


screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')
GAME_ON = True
while GAME_ON:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        segment_x = segments[seg_num - 1].xcor()
        segment_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(segment_x, segment_y)

    segments[0].forward(20)


screen.exitonclick()
