from turtle import  Turtle

FONT1 = ("Arial", 30, "normal")
FONT2 = ("Arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.num_chances = 10
        self.score = 0
        self.goto(x= -300, y= 220)
        self.update_score()

    def update_score(self, bool= ""):
        self.clear()
        if bool == True:
            self.score += 1
        elif bool == False:
            self.num_chances -=1
        else:
            pass
        self.write(arg= f"Score : {self.score} (#{self.num_chances} chances left)", font=FONT2)


    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write(arg= "Game Over", font=FONT1)

    def get_num_chances(self): return self.num_chances