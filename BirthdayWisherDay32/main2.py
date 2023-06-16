##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import datetime as dt
import re # to find and update [NAME] parts with a user name use regular expressions
import smtplib

#todays date
now = dt.datetime.now()
m_day = now.today().day # follows the pattern (year, month, day, hour, minutes, seconds)
m_month = now.today().month
today_tuple = (m_month, m_day)

# read dates in CSV
df = pd.read_csv("birthdays.csv")

myRow = []
print(f"TODAY TUPLE{today_tuple}")
for index, row in df.iterrows(): # iterate over the data frame
    month_day_tuple = (row['month'], row['day'])
    if month_day_tuple == today_tuple:
        myRow = row

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if len(myRow) != 0:
    print("pattern found")
    personName = myRow['name']
    personEmail = myRow['email']
    Sender = 'Enes' # change this to your own will
    letter_path  =f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_path, "r") as letter:
        letter_text = letter.read()
    # Define the patterns and their respective replacements
    patterns = {
        r'\[NAME\]': personName,
        r'\[Sender\]': Sender,
        # Add more patterns and replacements as needed
    }
    # Replace the patterns in the text
    for pattern, replacement in patterns.items():
        letter_text = re.sub(pattern, replacement, letter_text)

    msg_to_send = letter_text
    # no need to update the original letter

# 4. Send the letter generated in step 3 to that person's email address.

    sender = "@gmail.com" # chage this to your own will
    my_password = ""# your email password or a special pass given by your email for 3rd party apps

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()   #transport layer security , message encrypted
        connection.login(user=sender, password= my_password)
        connection.sendmail(from_addr=sender, to_addrs=personEmail , msg=f"Subject: Happy Birthday\n\n{msg_to_send}")
    print("Message successfully sended")


