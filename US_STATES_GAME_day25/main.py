import pandas
from turtle import Turtle , Screen
from state import State
import time
from score_board import Score

# screen setup
m_Screen = Screen()
m_Screen.title("U.S STATE GAME")
m_Screen.setup(width=720, height=500)
m_Screen.bgpic(picname="img/blank_states_img.gif")
m_Screen.tracer(0)
score_turtle = Turtle()
# getting Data from the data file and formatting it

states_data = pandas.read_csv("data/50_states.csv")

# creating a score board
m_Score = Score()


#Instead of creating a turtle for every state just create them when user knows the correct state name

# this way program will be faster and take less space
# states =[]
# def create_states():
#
#         for row in states_data.itertuples():
#             #print(row)
#             #new_state = State(state_name = row[1], xcor=row[2], ycor=row[3]) just create states
#             # if user knows the correct ans
#             states.append(new_state)
#         # rows are in the tuples form : Pandas(Index=42, state='Texas', x=-38, y=-106)
#
# create_states()

ans_correct = False
game_is_on = True

states_known = []
states_to_learn = []

while game_is_on:
    #m_Screen.update()
    #time.sleep(0.1)
    your_ans = m_Screen.textinput(title="Hello", prompt="Give a state name").title()
    #for state in states:
    for row in states_data.itertuples():
        if your_ans == row[1]:
            new_state = State(state_name = row[1], xcor=row[2], ycor=row[3])
            new_state.appear()
            ans_correct = True
            states_known.append(row[1])

    m_Score.update_score(ans_correct) # update the score accordingly

    if m_Score.get_num_chances() == 0:
        game_is_on = False
        m_Score.game_over()

    ans_correct = False

# iterate over the csv data and append the state names which were not known by the user
for row in states_data.itertuples():
    if not row[1] in states_known:
        states_to_learn.append(row[1])

# write these unknown states to csv file
df = pandas.DataFrame(states_to_learn)
df.to_csv("Data/states_to_learn.csv")



m_Screen.exitonclick()




