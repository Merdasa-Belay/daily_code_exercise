from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 274)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
