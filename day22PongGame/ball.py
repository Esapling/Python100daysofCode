import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.move_speed = 0.1
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_xcor = self.xcor() + self.move_x
        new_ycor = self.ycor() + self.move_y
        self.goto(x=new_xcor, y=new_ycor)

    def bounce_y(self):
        """
        this method allows the ball to reflect either from the walls or paddles
        """
        self.move_y *= -1
        # from +10 to -10 from -10 to +10
    def bounce_x(self):
        """
        this method allows the ball to reflect either from the walls or paddles
        """
        self.move_x *= -1
        self.move()
        # from +10 to -10 from -10 to +10


    def restart(self):
        self.bounce_x()
        self.goto(x=0, y=0)
        self.move_speed = 0.1

    def run(self):
        """
        this method changes the speed of updating time the screen so that playing the game becomes a bit harder after
        each hit to the paddles
        """
        self.move_speed *= 0.9
