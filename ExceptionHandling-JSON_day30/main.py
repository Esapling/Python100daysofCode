import tkinter
import file_opt
import random
from tkinter import messagebox
import pyperclip
from datetime import datetime
from os import linesep

# date

# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
current_time = now.strftime("%d/%m/%Y %H:%M:%S")


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

# functions
def reset_entry_boxes():
    user_entry.delete(first=0,last="end")
    password_entry.delete(first=0, last="end")
    web_entry.delete(first=0, last="end")
    user_entry.insert(0,string="fidan20@itu.edu.tr")
    
    
def ErrorPopUp():
    messagebox.showwarning(message="Please fill all the entriess")

def add_new_password():
    m_user = user_entry.get()
    m_web_name = web_entry.get()
    m_web_name = m_web_name.lower()
    print("web name:" + m_web_name)
    m_password = password_entry.get()
    
    data_dict = {
        m_web_name: {
            "user_name": m_user,
            "password":m_password,
            "update date":current_time,
        }
    }
    if m_user== "" or m_web_name == "" or m_password == "":
        ErrorPopUp()
    else:
        answer = messagebox.askokcancel(title= web_entry, message=f"Details entered: Website: {m_web_name}"
                           f" Username: {m_user}\nPassword: {m_password}\n Are sure you want to save ?")
        if answer:              
            file_opt.write(data_dict)
            messagebox.showinfo(title="Done",message="Data saved successfully!!")
            reset_entry_boxes()
        else:
            reset_entry_boxes()
    
def generate_password():
    # if user doesnt like the pass and cliks again delete the text entry
    password_entry.delete(first=0, last="end")
    my_pass = ""
    for _ in range(15):
        index = random.randint(33,127)
        pass_char = chr(index)
        my_pass += pass_char 
    password_entry.insert(0, string=my_pass)
    pyperclip.copy(my_pass)
    
def Search():
    m_web_name = web_entry.get()
    m_web_name = m_web_name.lower()
    print(m_web_name)
    result = file_opt.Search(m_web_name)
    if result == -1:
        messagebox.showwarning(message="Data is not found")
    else:
        info = f"{result['user_name']}\nPassword: {result['password']}\nLast update: {result['update date']}"
        messagebox.showinfo(title = m_web_name ,message=info)
        if messagebox.askyesno(message="Click ok to copy the password"):
            pyperclip.copy(result['password'])
            messagebox.showinfo(message="Password copied successfully")
        
    


#window configurations
window = tkinter.Tk()
window.minsize(620,500)
window.title("Password Manager")
window.configure(background=BG_COLOR_1, padx=20, pady=20)



# setting up canvas background photo grid 0-2
bg_canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0 )
bg_image = tkinter.PhotoImage(file="img/lock2.png")
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
user_entry.insert(0,string="fidan20@itu.edu.tr")




#label password 
password_label = tkinter.Label(bg=BG_COLOR_1)
password_label.config(text="Password", width=WIDTH_LABEL, height=HEIGHT_LABEL, font=FONT)
password_label.grid(row=3, column=0)

#password entry
password_entry = tkinter.Entry(width=55, borderwidth=2)
password_entry.configure(highlightthickness=3, highlightcolor=BG_COLOR_4)
password_entry.grid(row=3, column=1)


    
#button generate
generate_btn = tkinter.Button(width=18, height=2, text="GENERATE PASSWORD", font=("Arial", 9, "bold"), bg=BG_COLOR_2)
generate_btn.configure(command=generate_password)
generate_btn.grid(row=3, column=2)
#generate button



#button add
add_bttn = tkinter.Button(width=60, height=1, text="ADD", font= FONT, bg=BG_COLOR_2)
add_bttn.grid(row=4, column=0,columnspan=3, pady=10)
add_bttn.configure(command=add_new_password)

#search add
search_bttn = tkinter.Button(width=10, height=2, text="SEARCH", font= FONT, bg=BG_COLOR_2)
search_bttn.grid(row=1, column=3, padx=5)
search_bttn.configure(command=Search)



window.mainloop()






