import tkinter as tk
import pandas , pathlib
import pandas as pd
import random, time
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"

TXT_FONT = ("Times", 35, "bold")
CANVAS_WITDH = 400
CANVAS_HEIGHT = 300

IMG_X = 200
IMG_Y = 150
TITLE_Y = 50

#-------------------------------------WINDOW CONFIGURATION----------------------------#
window = tk.Tk()
window.title("QuizSet")
window.configure(bg=BACKGROUND_COLOR, padx=30, pady=30)
# setting up canvas background photo grid 0-2
my_canvas = tk.Canvas(width=CANVAS_WITDH, height=CANVAS_HEIGHT)
front_img = tk.PhotoImage(file="images/card_front.png")
back_img = tk.PhotoImage(file="images/card_back.png")
background_img = my_canvas.create_image(IMG_X, IMG_Y, image=front_img)
canvas_title = my_canvas.create_text(IMG_X,TITLE_Y, justify=tk.CENTER, text="TITLE", font=TXT_FONT, fill="black")
canvas_txt = my_canvas.create_text(IMG_X, IMG_Y, justify=tk.CENTER, text="WORD", font=TXT_FONT,
                   fill="black")  # first two number x,y coordinates
my_canvas.grid(row=0, column=1, columnspan=2, padx=100)


#----------------------------------------------Buttons----------------------------#
# tick
tick_img = tk.PhotoImage(file="images/right.png")
tick_bttn = tk.Button(image=tick_img, highlightthickness=0)
# tick_bttn.configure(width=50, height=50, pady=10)
tick_bttn.grid(row=1, column=2, padx=20, pady=20)
#cross
cross_img = tk.PhotoImage(file="images/wrong.png")
cross_bttn = tk.Button(image=cross_img, highlightthickness=0)
cross_bttn.grid(row=1, column=1, padx=20, pady=20)




#-----------------------------------READING CSV-------------------------------------#

data = pd.read_csv("first500.csv", encoding='utf-8').dropna()
wordList = data.to_dict(orient="records")  # a list of dictionaries
current_word = ""
known_words = []


#--------------------------------GET THE PROGRESS IF ANY --------------#
try:
    data = pandas.read_csv("progress/known_words.csv", encoding="utf-8-sig").dropna()
    known_words = data.to_dict(orient="records")
except FileNotFoundError:
    pass # pass simply if no progress exist

#-----------------------------------FUNCTIONS-------------------------------------#

def showMeaning():
    my_canvas.itemconfig(background_img, image= back_img)
    my_canvas.itemconfig(canvas_title, text="Turkish", fill="white")
    my_canvas.itemconfig(canvas_txt, text=current_word["Meaning"], fill = "white")

# after 3 secs show meaning function will be called
timer = window.after(3000, showMeaning)
def getNewList():
    global wordList
    path = pathlib.Path("data/newWords.csv")
    data = pd.read_csv(path, encoding='utf-8-sig').dropna()
    wordList = data.to_dict(orient="records")  # new list of words


def getWord():
    global current_word, timer
    window.after_cancel(timer) # for each new word reset the timing process so new session for a new card
    if len(wordList) == 0:
        ans = messagebox.askyesno("Well Done, You have learnt all the words\nClick 'yes' to get a new word list or no"
                                  "to no to exit?")
        if ans == "yes":
            getNewList()
        else:
            window.destroy() # destroy window
    Continue =True
    while Continue: # loop until getting an appropriate word
        word = random.choice(wordList)
        if not word in known_words:
            Continue = False
    my_canvas.itemconfig(background_img, image=front_img)
    my_canvas.itemconfig(canvas_title, text="English", fill="black")
    my_canvas.itemconfig(canvas_txt, text=word["Definition"], fill="black")
    current_word = word
    timer = window.after(3000, showMeaning)


def Success():
    known_words.append(current_word)
    wordList.remove(current_word) # remove the known word from source csv
    getWord()


tick_bttn.config(command=Success)
# when user dont know the words program will simply generate another word
cross_bttn.config(command=getWord)
#simply gets another word if user fails
#-------------------------------START PROGRAM---------------------#
# start the program by taking a word
getWord()

#----------------------------SAVE THE PROGRESS -------------------#
window.mainloop()
# after destroying window save the progress
data = pandas.DataFrame(known_words)
data.to_csv("progress/known_words.csv", encoding="utf-8-sig",index=False) # just utf-8 encoding wasnt working properly

