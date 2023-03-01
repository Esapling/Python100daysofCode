import turtle
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #  sets background color to black


#off the screen so that basic drawing is not showed to the user
screen.tracer(0)
snake = Snake()
food = Food()
myScore = Score()


screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_right, key="Right")


game_is_on = True
while game_is_on:
    #update screen
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        myScore.increaseScore()
        print("nom nom nom")
        food.refresh()
        snake.resize()
    # detect collisions with the Walls
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        myScore.game_over()

    # detect collisions with its body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            myScore.game_over()



screen.exitonclick()
