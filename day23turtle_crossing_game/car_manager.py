import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "white"] # random colors for the car turtle
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    def __init__(self, car_speed):
        super().__init__()
        self.penup()
        self.car_speed = car_speed

    def create_car(self):
        """
        creates new car on the left edge of the screen and at the random y location
        :return: none
        """
        pos_x = -270
        pos_y = random.randint(-260, 280)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=0.6, stretch_len=1.2)
        self.setposition(x=pos_x, y=pos_y)

    def move(self):
        """
        moves the cars along the x-axis
        :return: none
        """
        new_x = self.xcor() + self.car_speed
        curr_y = self.ycor()    # no change cars will move horizontally
        self.penup()
        self.goto(x=new_x, y=curr_y)


