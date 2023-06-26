from turtle import Turtle, Screen



class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.create_ball()
  def create_ball(self):
    self.shape("square")
    self.shapesize(stretch_wid=1, stretch_len=1)
    self.color("white")
    