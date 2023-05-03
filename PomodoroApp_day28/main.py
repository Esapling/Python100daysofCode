import tkinter
import time
from totalWorkDays import howManyReps


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("POMODORO")
#geometry function doesnt limit the min size you can make it as small as you want
# if you want to set a minsize then use min size method
#window.geometry("420x300")
window.minsize(width=350, height=350)
window.configure(padx=30, pady=30, background=YELLOW)

#Canvas Timer text
canvas = tkinter.Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)  # to remove border highlighthickness
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato) #
timer_txt = canvas.create_text(100,140, text="30:00", fill="white", font=("Arial", 40,'bold'))
canvas.grid(row=1, column=1)

# Timer Label
timer_label = tkinter.Label(text="Timer")
timer_label.config(fg="black",bg=YELLOW, font=("Arial", 30, 'bold'))
timer_label.grid(row=0,column=1)


#button start
start_btn = tkinter.Button(text="Start", font=("Arial",7, 'bold'), bg="white")
#start_btn.place(height=20, width=40, anchor='nw', s)
start_btn.config(width=8, height=4)
start_btn.grid(row=2, column=0)

#button restart
reset_btn = tkinter.Button(text="Reset",font=("Arial", 7, 'bold'), bg="white")
#reset_btn.place(height=20, width=40, anchor='se')
reset_btn.config(width=8, height=4)
reset_btn.grid(row=2, column=2)




#check mark label
check_mark = tkinter.Label(bg=GREEN, font=("Arial",8))
check_mark.grid(row=2, column=1)

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


#starting_time = "30:00"
def countDown(total_time):
    total_time -= 1
    min =  int(total_time / 60)
    seconds = total_time % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_txt, text=f"{min}:{seconds}")
    if total_time> 0:
        global timer
        timer = window.after(1000, countDown, total_time)
    else:
        start_timer()


def start_timer():
    global reps
    reps += 1
    work_session = WORK_MIN * 60
    short_break_session = SHORT_BREAK_MIN* 60
    long_break_session = LONG_BREAK_MIN *60
    if reps % 8 == 0:
        timer_label.config(text="FOCUS", font=("Arial", 30, 'bold'), fg="RED")
        countDown(long_break_session)
    elif reps % 2== 0:
        timer_label.config(text="BREAK", font=("Arial", 30, 'bold'), fg="BLUE")
        countDown(short_break_session)
    else:
        timer_label.config(text="FOCUS", font=("Arial", 30, 'bold'), fg="RED")
        countDown(work_session)
        textCheck = ''
        for i in range(int(reps/2)):
            textCheck += '✔'
        check_mark.configure(text= textCheck)


    start_btn.configure(state="disabled")
    reset_btn.configure(state="active")

def reset():
    global  reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    check_mark.configure(text="")
    timer_label.configure(text="Timer")
    reset_btn.configure(state="disabled")
    start_btn.configure(state="active")
    howManyReps(int(reps)/2, WORK_MIN, SHORT_BREAK_MIN)
    reps = 0


start_btn.configure(command=start_timer)
reset_btn.configure(command=reset)

#countDown(total_time)













window.mainloop()
