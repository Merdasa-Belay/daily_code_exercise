from turtle import Turtle, Screen

screen = Screen()
START = [(0, 0), (-20, 0), (-40, 0), ]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.player_square = []
        self.create_snake()
        self.head = self.player_square[0]

    def create_snake(self):
        for cordx in START:
            self.player = Turtle()
            self.player.shape("square")
            self.player.color("white")
            self.player.penup()
            self.player.goto(cordx)
            self.player_square.append(self.player)

    # def up(self):
    #     """
    #     travel's up
    #     """
    #     if self.head.setheading() != DOWN:
    #         self.head.setheading(UP)

    # def down(self):
    #     if self.head.setheading() != UP:
    #         self.head.setheading(DOWN)

    # def left(self):
    #     if self.head.setheading() != RIGHT:
    #         self.head.setheading(LEFT)

    # def right(self):
    #     if self.head.setheading() != LEFT:
    #         self.head.setheading(RIGHT)

    def up(self):
        """
        travel's up
        """

        self.head.setheading(UP)

    def down(self):

        self.head.setheading(DOWN)

    def left(self):

        self.head.setheading(LEFT)

    def right(self):

        self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.player_square) - 1, 0, -1):
            new_x = self.player_square[seg_num - 1].xcor()
            new_y = self.player_square[seg_num - 1].ycor()
            self.player_square[seg_num].goto(new_x, new_y)

        self.player_square[0].forward(MOVE_DISTANCE)
