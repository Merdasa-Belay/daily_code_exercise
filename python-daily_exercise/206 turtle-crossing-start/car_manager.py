from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.goto(270, random.randint(-250, 250))
        self.all_cars.append(car)
        self.move()

    def move(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)
