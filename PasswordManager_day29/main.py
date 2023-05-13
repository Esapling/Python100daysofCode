import tkinter
import file_opt
import random

# some inital constants
BG_COLOR_1 = "#3a5158"
BG_COLOR_2 = "#91cadb"
BG_COLOR_3 = "#597c86"
BG_COLOR_4 = "#66fc3d"
BG_COLOR_5 = "#1f7a06"
FONT = ("Arial", 10, 'bold')
WIDTH_ENTRY = 80
WIDTH_LABEL = 14
HEIGHT_LABEL = 3


#window configurations
window = tkinter.Tk()
window.minsize(600,450)
window.title("Password Manager")
window.configure(background=BG_COLOR_1, padx=20, pady=20)



# setting up canvas background photo grid 0-2
bg_canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0 )
bg_image = tkinter.PhotoImage(file="img/logo.png")
bg_canvas.create_image(100, 100, image= bg_image)
bg_canvas.grid(row=0, column=1)


#label website_name 
website_name_label = tkinter.Label()
website_name_label.config(borderwidth=5, text="Web site name", width=WIDTH_LABEL, height=HEIGHT_LABEL, background=BG_COLOR_1, font=FONT)
website_name_label.grid(row=1, column=0)
#web entry
web_entry = tkinter.Entry(width=WIDTH_ENTRY, borderwidth=2)
web_entry.configure(highlightthickness=3, highlightcolor=BG_COLOR_4)
web_entry.grid(row=1, column=1, columnspan=2)




#label user_name 
user_name_label = tkinter.Label()
user_name_label.config(borderwidth=0, text="Username/Email", width=WIDTH_LABEL, height=HEIGHT_LABEL, bg=BG_COLOR_1,font=FONT)
user_name_label.grid(row=2, column=0)


#user_name entry
user_entry = tkinter.Entry(width=WIDTH_ENTRY, borderwidth=2)
user_entry.configure(highlightthickness=3, highlightcolor=BG_COLOR_4)
user_entry.grid(row=2, column=1, columnspan=2)





#label password 
password_label = tkinter.Label(bg=BG_COLOR_1)
password_label.config(text="Password", width=WIDTH_LABEL, height=HEIGHT_LABEL, font=FONT)
password_label.grid(row=3, column=0)

#password entry
password_entry = tkinter.Entry(width=55, borderwidth=2)
password_entry.configure(highlightthickness=3, highlightcolor=BG_COLOR_4)
password_entry.grid(row=3, column=1)


def reset_entry_boxes():
    user_entry.delete(first=0,last="end")
    password_entry.delete(first=0, last="end")
    web_entry.delete(first=0, last="end")
    
def errorPopUp():
    new_win = tkinter.Toplevel()
    new_win.geometry("200x120")
    new_win.title("Opps")
    tkinter.Label(new_win, text="Please Fill the all entries!!!" , font=FONT).pack()

def add_new_password():
    user = user_entry.get()
    web_name = web_entry.get()
    m_password = password_entry.get()
    if user== "" or web_name == "" or m_password == "":
        errorPopUp()
    else:
        file_opt.write(web_site=web_name, user_name=user, string_password= m_password)
        reset_entry_boxes()
    
def generate_password():
    # if user doesnt like the pass and cliks again delete the text entry
    password_entry.delete(first=0, last="end")
    my_pass = ""
    for _ in range(10):
        index = random.randint(33,127)
        pass_char = chr(index)
        my_pass += pass_char 
    password_entry.insert(0, string=my_pass)
    

    
#button generate
generate_btn = tkinter.Button(width=18, height=2, text="GENERATE PASSWORD", font=("Arial", 9, "bold"), bg=BG_COLOR_2)
generate_btn.configure(command=generate_password)
generate_btn.grid(row=3, column=2)
#generate button



#button add
add_bttn = tkinter.Button(width=60, height=1, text="ADD", font= FONT, bg=BG_COLOR_2)
add_bttn.grid(row=4, column=0,columnspan=3, pady=10)
add_bttn.configure(command=add_new_password)



window.mainloop()






