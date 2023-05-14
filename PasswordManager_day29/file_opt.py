from datetime import datetime
from os import linesep

# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
time_in_format = now.strftime("%d/%m/%Y %H:%M:%S")


def write(web_site, user_name,string_password):
    password_file = open("my_passwords.txt", "a")
    password_file.write(web_site + " | ")
    password_file.write(user_name + " | password: ")
    password_file.write(string_password + " Tarih: ")
    password_file.write(time_in_format + linesep) 
    password_file.close()
    
