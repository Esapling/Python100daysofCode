from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.starting_x = 0
        self.starting_y = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.create_segment()

    def create_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        self.segments.append(new_segment)
        new_segment.goto(x=self.starting_x, y=self.starting_y)
        self.starting_x -= 10

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            # move the segments from last to first and then
            # move the first segment wherever you want to go
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
            # 1 2 3 _> start = 1 stop = 3 step = 1
            # 3 2 1 -> start = 3 stop = 1 step = -1
            # new_x = segment[2-1].xcor()
            # segment[2].goto() move third segment to the 2's prev place
        self.head.forward(20)

    #arrow keys doesnt move the snake they will just let you change the heading of the snake
    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(90)
    def turn_left(self):
        if not self.head.heading()== RIGHT:
            self.head.setheading(180)
    def turn_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(0)
    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(270)

    def resize(self):
        self.create_segment()



