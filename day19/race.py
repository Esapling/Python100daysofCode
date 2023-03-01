import random
import turtle
from turtle import Turtle, Screen

"""
purpleTurtle = Turtle(shape="turtle")
blueTurtle = Turtle(shape="turtle")
blackTurtle = Turtle(shape="turtle")
yellowTurtle = Turtle(shape="turtle")
purpleTurtle.color("purple")
purpleTurtle.goto(x=-240, y=-100)
blueTurtle.color("blue")
blueTurtle.goto(x=-250,y=-0)
blackTurtle.color("black")
blackTurtle.goto(x=-250,y=50)
yellowTurtle.color("yellow")
yellowTurtle.goto(x=-240,y=150)
"""
screen = Screen()
screen.bgcolor(0.5,0.2,0.5)

def race():
    global screen
    screen.setup(width=500, height=400)
    your_bet= screen.textinput(title="Make your bet!", prompt="Which one will win the race? (red,orange,yellow,green,blue,purple")
    colors = ["red","orange","yellow","green","blue","purple"]
    turtles = []
    startingX = -240
    startingY = -100
    for c in colors:
        newTurtle = Turtle(visible=True, shape="turtle")
        newTurtle.color(c)
        newTurtle.penup()
        newTurtle.speed(4)
        turtles.append(newTurtle)
        newTurtle.goto(x= startingX, y=startingY)
        startingY += 40

    race_end = startingX * -1 #last point
    while True:
        for _turtle in turtles:
            rand_dist = random.randint(0,15)
            _turtle.forward(rand_dist)
            currentPos = _turtle.position()
            currentCol = _turtle.color()
            #print(f"Current pos {currentPos}")
            if currentPos[0] >= race_end:
                if currentCol[0] == your_bet:
                    screen.title(f"Turtle {currentCol[0]} wins the race, Well Done you got it")
                else:
                    screen.title(f"Turtle {currentCol[0]} wins the race, You lose ")
                return
            else:
                continue

race()
screen.exitonclick()
