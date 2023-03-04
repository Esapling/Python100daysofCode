from turtle import Turtle

LENGTH = 1
WIDTH = 3.7

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.goto(position)

    def up(self):
        new_ycor = self.ycor() + 20
        if new_ycor < 280:
            self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        if new_ycor > -280:
            self.goto(self.xcor(), new_ycor)

