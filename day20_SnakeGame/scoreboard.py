# a scoreboard class that calculates score and shows it on the screen

from turtle import Turtle, Screen
FONT =("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.write(arg=f"Score: {self.score}", align='center', font = FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align='center', font = FONT)

    def getScore(self):
        return self.score

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", font=FONT)
