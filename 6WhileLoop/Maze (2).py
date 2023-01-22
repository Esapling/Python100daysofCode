def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left() 
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
#here the hint is to follow the right path as much as possible and if not going forward if possible 
#else turning left and checking the conditions again
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

