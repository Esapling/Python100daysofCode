# a small miles to km converter with tkinter 

import tkinter


window = tkinter.Tk()
window.minsize(width=200, height= 200)
window.config(background="#FE6244")



#label
title = tkinter.Label(text="Miles", font=("Serif", 20, "bold"), background="#FE6244", width=10, border=4)
title.grid(column=0, row=1)


# km label
km_label = tkinter.Label(text="0")
km_label.config(font=("Serif", 16, "bold"), border=4, width=20, background="light yellow")
km_label.grid(column=1, row=2)


# km label
km_label_text = tkinter.Label(text="Result: ")
km_label_text.config(font=("Serif", 20, "bold"), background="#FE6244", width=10, border=4)
km_label_text.grid(column=0, row=2)


miles = 0
output_km = 0
def get_value():
    global output_km 
    miles =  float(input_miles.get())
    output_km = 1.60934 * float(miles)
    km_label.config(text=f"{output_km:.2f} kilometer")
    


#i/o boxes
input_miles = tkinter.Entry(width=50)
input_miles.config(background="light yellow", border=4)
#input_miles.bind("<Return>", get_value)
#input_miles.insert(tkinter.END,"Enter miles and click Return key: ")
input_miles.grid(column=1, row=1)
#convert input miles to km


# send button
button = tkinter.Button(text="Convert", width=20, command=get_value)
button.config(bg="red", border=5)
button.grid(column=2, row=1)


window.mainloop()