import random
import smtplib
import datetime as dt
my_email = ""
my_password = "" # write here your email password


def send(msg, receiver):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() #transport layer securtiy , message encrypted
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver, msg=f"Subject:Hello\n\n{msg}")

def getMessage():
    with open("quotes.txt", "r") as quotes:
        quoteList = quotes.readlines()
        #print(quoteList[4])
        random_msg = random.choice(quoteList)
        return random_msg


now = dt.datetime.now()
day_of_week = now.weekday()

receiver = ""


print(day_of_week)
if day_of_week == 1:
    msg = getMessage()
    send(msg, my_email)