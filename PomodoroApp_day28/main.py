import tkinter
import time
from tkinter import messagebox
from totalWorkDays import howManyReps
from PIL import ImageTk, Image   

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_LABEL=('calibre',10, 'bold')

DEFAULT_WORK = 30
DEFAULT_SHORT_BREAK_MIN = 3
DEFAULT_LONG_BREAK_MIN = 5
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

main_window = tkinter.Tk()
main_window.title("POMODORO")
#geometry function doesnt limit the min size you can make it as small as you want
# if you want to set a minsize then use min size method
#main_window.geometry("420x300")
main_window.minsize(width=750, height=500)
main_window.configure(padx=30, pady=30, background=YELLOW)

#Canvas Timer text
canvas = tkinter.Canvas(width=400, height=450, bg=YELLOW, highlightthickness=0)  # to remove border highlighthickness
tomato = tkinter.PhotoImage(file="tomato.resized.png")
canvas.create_image(200, 212, image=tomato) #
timer_txt = canvas.create_text(200,240, text="30:00", fill="white", font=("Arial", 40,'bold'))
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



#------------------------------------Open A New Window For Timer Configuration---------------#

total_time_tuple = ()

# an image for new window
#img_config = tkinter.PhotoImage(file="config.png")
img_config = Image.open("config.png")
    
def Config():
    new_window = tkinter.Toplevel(master=main_window)
    new_window.title("Configuration")
    new_window.config(background=GREEN)
    new_window.minsize(width=800, height=800)
    
    work_label = tkinter.Label(new_window, text="Work Time", width=15,background=PINK, font=FONT_LABEL)
    work_label.grid(row=0,column=0)
    work_entry = tkinter.Entry(new_window ,width=15)
    work_entry.grid(row=0, column=1)

    long_break_label = tkinter.Label(new_window, text="Long Break Time", width=15, font=FONT_LABEL, bg=PINK)
    long_break_label.grid(row=1,column=0)
    long_break_entry = tkinter.Entry(new_window,textvariable="Enter short long duration in minutes: ", width=15)
    long_break_entry.grid(row=1, column=1)

    short_break_label = tkinter.Label(new_window, text="Short Break Time", width=15, font=FONT_LABEL, bg=PINK)
    short_break_label.grid(row=2,column=0)
    short_break_entry = tkinter.Entry(new_window,textvariable="Enter short break duration in minutes: ", width=15)
    short_break_entry.grid(row=2, column=1)

    #-------------Configuration Image --------#
    test = ImageTk.PhotoImage(img_config)

    label1 = tkinter.Label(new_window,image=test, highlightthickness=0)
    label1.image = test

    # Position image
    #label1.place(x=0, y=-40)
    label1.grid(row=5, column=0, columnspan=3, padx=40, pady=50)

    def Ok():
        global total_time_tuple
        work_session = int(work_entry.get())
        long_break_session= int(long_break_entry.get())
        short_break_session = int(short_break_entry.get())
        total_time_tuple = (work_session, long_break_session, short_break_session)
        
        new_window.destroy() # save and return

    button_accept = tkinter.Button(new_window, background=RED, width=10, text="OK", command=Ok)
    button_accept.grid(row=1, column=2)



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
        timer = main_window.after(1000, countDown, total_time)
    else:
        start_timer()


def start_timer():
    global reps
    reps += 1
    if total_time_tuple == (): # if user goes with the default values
        work_session = DEFAULT_WORK* 60
        short_break_session = DEFAULT_SHORT_BREAK_MIN* 60
        long_break_session = DEFAULT_LONG_BREAK_MIN*60
    else:
        work_session = total_time_tuple[0] * 60
        short_break_session = total_time_tuple[1]* 60
        long_break_session = total_time_tuple[2]*60

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
    main_window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    check_mark.configure(text="")
    timer_label.configure(text="Timer")
    reset_btn.configure(state="disabled")
    start_btn.configure(state="active")
    if total_time_tuple == ():
        howManyReps(int(reps)/2, DEFAULT_WORK, DEFAULT_SHORT_BREAK_MIN)
    else:
        howManyReps(int(reps)/2, total_time_tuple[0], total_time_tuple[1])
    reps = 0


button_config = tkinter.Button(background='white',text="Configure", width=15, command=Config)
button_config.grid(row=3, column=1)



messagebox.showinfo(title="Notification", message="Current Work, short and long break time as following:30,3,5\nIn order to "
                    "change the values please click on the configure button 'Before' starting to a new session")


start_btn.configure(command=start_timer)
reset_btn.configure(command=reset)


main_window.mainloop()
