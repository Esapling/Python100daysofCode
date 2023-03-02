from turtle import Turtle, Screen
from ball import Ball
from players import Player
from screenboard import Score
import time

# our constants
SCORE_POS1 = (-60, 280)
SCORE_POS2 = (+60, 280)
PLAYER_POS1 = (-380,0)
PLAYER_POS2 = (380,0)


# initalize screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# instantiate Players
player1 = Player(PLAYER_POS1)
player2 = Player(PLAYER_POS2)

# instantiate Score objects
score1 = Score(SCORE_POS1)
score2 = Score(SCORE_POS2)

# instantiate Ball object
ball = Ball()


screen.listen()
screen.onkey(player1.up, "Up")
screen.k
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with the upper or below wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.run()
    # detect collision with the right paddle
    if (ball.distance(player1) < 50 and ball.xcor() < -320) or (ball.distance(player2) <50 and ball.xcor() > 320):
        ball.bounce_x()
        ball.run()
    elif ball.xcor() > 350:
        ball.restart()
        score1.increase_score()
    elif ball.xcor() < -350:
        ball.restart()
        score2.increase_score()

screen.exitonclick()

