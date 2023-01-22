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
checkPoint = 0 # a small memory to detect if we just drawing a circle around :)
while not at_goal():
    if right_is_clear():
        if not checkPoint == 4:
            turn_right()
            move()
            checkPoint +=1
        else:
            if front_is_clear(): #we shouldnt just hit a wall while trying to get rid of a loop
                move()
                checkPoint= 0
            else: 
                turn_left()
    elif front_is_clear():
        checkPoint =0
        move()
    else:
        checkPoint = 0
        turn_left()
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

