import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
player1 = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player1.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()
# TODO Detectin the collision with the car
    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            game_is_on = False

# TODO Detect a successful crossing

    if player1.is_at_finish_line():
        player1.go_to_start()
        car_manager.level_up()


screen.exitonclick()
