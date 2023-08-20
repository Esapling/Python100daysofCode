from data_manager import DataManager



user_name = input("Welcome, please enter your first name: ")
user_lastname = input("Your last name: ")
user_email = input("Enter your email: ")

user = {
    "name":user_name,
    "last_name":user_lastname,
    "email":user_email
}

data_manager = DataManager()

data_manager.addUserToSheet(user)

