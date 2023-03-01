import turtle
from turtle import Turtle , Screen

def move_up():
    karabas.forward(10)
def turn_right():
    newheading = karabas.heading() - 20
    karabas.setheading(newheading)
def move_down():
    karabas.backward(10)
def turn_left():
    newheading = karabas.heading() + 20
    karabas.setheading(newheading)

def clear():
    karabas.clear()
    karabas.penup()
    karabas.home()
    karabas.pendown()

newscreen = Screen()
karabas = Turtle()
karabas.speed("fastest")
turtle.colormode(255)


newscreen.listen() # tell the screen to listen to the events
#Set focus on TurtleScreen (in order to collect key-events)


newscreen.listen()


newscreen.onkey(fun=turn_right, key="d")
newscreen.onkey(fun=move_up, key="w")
newscreen.onkey(fun=move_down, key="s")
newscreen.onkey(fun=turn_left, key="a")

newscreen.onkey(fun=clear, key="c")


newscreen.exitonclick()