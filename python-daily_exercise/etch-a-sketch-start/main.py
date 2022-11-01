from turtle import Turtle, Screen

eyob = Turtle()
screen = Screen()
eyob.speed("fastest")

def forward():
    return eyob.forward(10)


def backward():
    return eyob.backward(10)

def clockwise():
    return eyob.right(10)
    
def anticlockwise():
    return eyob.left(10)

def clear_screen():
    eyob.clear()
    eyob.penup()
    eyob.home()

screen.listen()
# screen.onkey(key='space', fun=mov     e_forward)
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=clockwise)
screen.onkey(key='d', fun=anticlockwise)
screen.onkey(key='c', fun=clear_screen)


screen.exitonclick()
