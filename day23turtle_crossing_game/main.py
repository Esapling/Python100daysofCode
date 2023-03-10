import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")

player1 = Player()
screen.onkey(fun=player1.move, key="Up")
m_Scoreboard = Scoreboard()

game_is_on = True
cars = []
car_speed = 10
while game_is_on:
    screen.update()
    time.sleep(0.15)
    random_chance = random.randint(1, 4)
    # roll a die so that the screen doesn't mess up with lots of cars and,we can play
    if random_chance == 1:
        new_car = CarManager(car_speed)
        new_car.create_car()
        cars.append(new_car)
    for car in cars:
        car.move()
        if car.distance(player1) <= 20:
            game_is_on = False
            m_Scoreboard.game_over()
    # detect collisions
    if player1.check_win():
        m_Scoreboard.update_board()
        car_speed += 3
        # increase the incoming cars' speed to make it more challenging
    else:
        continue

screen.exitonclick()
