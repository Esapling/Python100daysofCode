from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(-260, 260)
        self.write(arg=f"Level: {self.score}", font=FONT)

    def update_board(self):
        """
        this function writes to the current level of the game to the given position
        :return: none
        """
        self.clear()
        self.score += 1
        self.write(arg=f"Level: {self.score}", font=FONT)

    def game_over(self):
        """
        this function writes to the screen YOU LOSE at the end of the game
        :return:
        """
        self.clear()
        self.goto(x=0, y=0)
        self.color("red")
        self.write(arg="YOU LOSE!", font=FONT)
