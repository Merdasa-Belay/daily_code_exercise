from turtle import Turtle, Screen

SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_index = []
        self.create_snake()
        self.head = self.snake_index[0]

    def create_snake(self):
        for position in SEGMENT_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg in range(len(self.snake_index) - 1, 0, -1):
            new_x = self.snake_index[seg - 1].xcor()
            new_y = self.snake_index[seg - 1].ycor()
            self.snake_index[seg].goto(new_x, new_y)

        self.head.forward(20)

    def add_segment(self, position):
        self.snake = Turtle()
        self.snake.color("white")
        self.snake.shape("square")
        self.snake.penup()
        self.snake.goto(position)
        self.snake_index.append(self.snake)

    def reset(self):
        self.snake_index.clear()
        self.create_snake()
        self.head = self.snake_index[0]

    def extend(self):
        # TODO add new segment to the snake
        self.add_segment(self.snake_index[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        self.head.goto(0, 0)
