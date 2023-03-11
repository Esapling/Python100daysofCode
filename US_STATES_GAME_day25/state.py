from turtle import Turtle

FONT = ("Arial", 8, "normal")

class State(Turtle):
    def __init__(self, state_name, xcor, ycor):
        super().__init__(visible=False)
        #if I dont add visible= False into the initializer , somehow my turtle is still being on the screen
        # even I use turtle.hide method
        # this might be about creation time of the objects so I added it to the constructor line(initializer)
        #now it works pretty well
        self.shape("square")
        self.penup()
        self.name = state_name
        self.pos_x = xcor
        self.pos_y = ycor


    def appear(self):
        self.goto(x= self.pos_x, y=self.pos_y)
        self.write(arg=f"{self.name}".capitalize(), font= FONT)

    def get_name(self): return self.name

    # def create_State(self, state_name, pos_x, pos_y):
    #     new_state = Turtle()
    #     new_state.penup()
    #     #new_state.goto(x=pos_x, y=pos_y)
    #     #new_state.write(arg=f"{state_name}")
