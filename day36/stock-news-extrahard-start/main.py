import requests
import os
from datetime import date, timedelta

from twilio.rest import Client


SENDER_NUM = os.environ['senderNum']
RECEIVER_NUM = os.environ['MyPhoneNum']
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_ALPHA_API_KEY = os.environ['ALPHA_API'] 

#hide your api key to your system using export command
#but it will be deleted if you close your system or terminal 
# to save it , write the command (i.e export=YOUR_API_KEY) to the .bashrc file 
# after that dont forget to close the terminal to see changes

#---------------------------------GETTING DATA---------------------------------#
alpha_api = "https://www.alphavantage.co/query?"
parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'interval':'5min',
    'apikey':MY_ALPHA_API_KEY,
    'outputsize':'compact'
}
response = requests.get(url=alpha_api, params=parameters)
response.raise_for_status()
data = response.json()

today = date.today()
yesterday = today - timedelta(days=1) 
the_day_before = yesterday - timedelta(days=3) 
# 3 days before yesterday is given after than yesterday, and then it goes back by 1 day for each data
# date should be in string format
yesterday = str(yesterday)
the_day_before = str(the_day_before)


data_yesterday = data['Time Series (Daily)'][yesterday]
data_the_day_before = data['Time Series (Daily)'][the_day_before]

change_in_price = float(data_yesterday['4. close']) - float(data_the_day_before['1. open'])

print(f"Change price is {change_in_price} , last close {data_yesterday['4. close']} and opening {data_the_day_before['1. open']}")


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def SEND_MSG():
    global change_in_price
    news_api = "https://newsapi.org/v2/everything?"
    MY_NEWS_API_KEY = os.environ['NEWS_API']
    parameters = {
        'q':COMPANY_NAME,
        'apikey':MY_NEWS_API_KEY,
    }
    response = requests.get(url=news_api, params=parameters)
    response.raise_for_status()
    data = response.json()
    descriptions = []
    titles = []

    #message entry
    message_body = ""
    if change_in_price >= 0:
        message_body = f"{COMPANY_NAME}: " + '🔺' + str(change_in_price) + '\n'
    else :
        message_body = f"{COMPANY_NAME}: " + '🔻' + str(change_in_price) + '\n'

    #message body
    for i in range(3): 
        titles.append(data['articles'][i]['title'])
        descriptions.append(data['articles'][i]['description'])
        message_body += 'Headline: ' + titles[i] + '\n' + 'Brief: ' + descriptions[i]
    
    #send message

    message = client.messages.create(from_=SENDER_NUM, to=RECEIVER_NUM, body= message_body)


if abs(change_in_price)/ float(data_yesterday['4. close']) > 0.05:
    SEND_MSG()
