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
while not at_goal():
    while not front_is_clear():
        up()
        right()
        down()
    if at_goal() != True:
        move()
# better solution 
#    while not at_goal():
#        if wall_is_front():
#            jump() // up right down
#        else:
#            move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

