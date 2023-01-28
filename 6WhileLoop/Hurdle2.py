def turn_right():
    turn_left()
    turn_left()
    turn_left()
def right():
    turn_right()
    move()
def up():
    turn_left()
    move()
def down():
    turn_right()
    move()
    turn_left()
def go_one_step():
    move()
    up()
    right()
    down()

def jump(x):
    for i in range(0,x):
        go_one_step()
# repetitive step right up right down right
# challange 2 you dont have the number of steps initally to reach the flag
while at_goal() != True:
    go_one_step()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
