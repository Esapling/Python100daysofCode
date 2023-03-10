from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.color("red")

    def move(self):
        """
        allows player turtle to move when player pressed to "UP" arrow key
        :return:
        """
        self.forward(MOVE_DISTANCE)

    def check_win(self):
        """
        checks whether the player turtle is across the road safely
        returns True if so , otherwise False
        """
        if self.ycor() >= FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            return True
        return False