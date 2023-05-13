#
def write(web_site, user_name,string_password):
    password_file = open("my_passwords.txt", "a")
    password_file.write(web_site + " | ")
    password_file.write(user_name + " | password: ")
    password_file.write(string_password)
    password_file.close()
    
