def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left() # since we know from the call that the wall is on our front
    while wall_on_right():# this will be called at least one time
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front(): # will go down 
        move()
    turn_left()
while not at_goal():  
    if not front_is_clear():
        jump()
    else:
        move()
    
            
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

