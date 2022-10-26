# from turtle import Turtle, Screen, forward

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(200)
# # timmy.speed(200)

# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable


table = PrettyTable()
# print(table)

table.add_column("Pokeman Name", ["Pickachu", "Squirtle", "Charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)
