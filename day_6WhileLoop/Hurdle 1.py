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

jump(6)    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
