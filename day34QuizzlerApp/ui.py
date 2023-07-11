import tkinter as tk
from quiz_brain import QuizBrain
from question_model import Question
#CONSTANTS
FONT_SCORE = ('arial',12,'italic')
IMG_X = 150
IMG_Y = 125
TXT_FONT = ("Roboto", 13, "italic")
CANVAS_WITDH = 500
CANVAS_HEIGHT = 450
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain : QuizBrain):
        self.quiz = quizbrain
        self.timer = None
        self.currentQuestOb : Question
        #-----------__WINDOW CONFIGURATION-----------------#
        self.window = tk.Tk()
        self.window.title("QuizzZime")
        self.window.minsize(width=600, height=700)
        self.window.config(background=THEME_COLOR, padx=50, pady=20)
        
        self.canvas = tk.Canvas(width=CANVAS_WITDH, height=CANVAS_HEIGHT, bg='white')
        self.canvas_txt = self.canvas.create_text(200,200, justify=tk.CENTER, text="Some Question", font=TXT_FONT,
                        fill="black", width=400)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50, padx=100)
        #--------------------SCORE TABLE ------------#
        #self.score = tk.StringVar()
        #self.score.set('Score : 0')
        self.score_label = tk.Label(text=f'Score {self.quiz.score}', background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        #------------TRUE FALSE IMAGES--------------#
        true_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")
        #--------------------TRUE FALSE BUTTONS-----------#
        self.bttn_true = tk.Button(image = true_img,command=lambda : self.checkAns('True'), highlightthickness=0)
        self.bttn_true.grid(row=2, column=2)
        self.bttn_false = tk.Button(image= false_img, command=lambda : self.checkAns('False'), highlightthickness=0)
        self.bttn_false.grid(row=2,column= 0)
        

        self.question_next()
        self.window.mainloop()

    #-----------------Function to get next question------------#
    def question_next(self): 
        # if user press a button before 1s then 'after method' which is called in chechAns method 
        # will still be in progress and it will call the question next method again  
        # to prevent this error just cancel the counting process whenever it enters this method
        if self.timer is not None:
            self.window.after_cancel(self.timer)
            # avoid the ValueError when attempting to cancel a timer that hasn't been initialized yet.
        if self.quiz.still_has_question():
            questionObj = self.quiz.next_question()
            self.canvas.itemconfigure(self.canvas_txt , text=(f"Q.{self.quiz.question_number}\n{questionObj.text}"))
            self.currentQuestObj = questionObj
        else:
            self.canvas.itemconfigure(self.canvas_txt, text='Well Done You have completed the quiz')
            self.bttn_false.config(state='disabled')
            self.bttn_true.config(state='disabled')



    def checkAns(self,answer):
        result = self.quiz.check_ans(self.currentQuestObj, answer)
        #check result
        if result:
            self.canvas.itemconfigure(self.canvas_txt , text='Well Done ')
        else:
            self.canvas.itemconfigure(self.canvas_txt , text='No it was False' if answer == 'True' else 'No it was True')
        #update score widget
        self.score_label.config(text= f"Score :{self.quiz.score}")
    # Call next question method after a delay of 1000 milliseconds to see the update since next method also updates the canvas
        self.timer = self.window.after(1000, self.question_next)  
