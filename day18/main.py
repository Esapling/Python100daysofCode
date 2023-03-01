import random
import turtle

import colorgram
from turtle import  Turtle, Screen
turtle.colormode(255)


m_Turtle = Turtle()

#screen starts
screen = Screen()
colors = colorgram.extract('image.jpg',number_of_colors=16)
m_Turtle.pen(shown=True)
m_Turtle.speed("slow")
m_Turtle.penup()
m_Turtle.hideturtle()
m_Turtle.setposition(-100,-100)

color_list = []
"""
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    newColor = (r,g,b)
    color_list.append(newColor)
print(color_list)
"""
#color list is rearranged so that white background colors arent shown
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199)]
#print(len(color_list))


def move_in_row():
    for _ in range(10):
        color = random.choice(color_list)
        #m_Turtle.pendown()
        m_Turtle.dot(20, color)
        m_Turtle.forward(50)




for i in range(10):
    m_Turtle.setposition(-200, -200+ i*50)
    move_in_row()



#screen ends
screen.exitonclick()
