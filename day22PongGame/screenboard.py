from turtle import Screen, Turtle

m_FONT = ('Arial', 14, 'normal')
class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.write(arg=f"Score: {self.score}", align="center", font=m_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=m_FONT)



