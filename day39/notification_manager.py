import requests
import os

from twilio.rest import Client



SENDER_NUM = os.environ['senderNum']
RECEIVER_NUM = os.environ['MyPhoneNum']
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']


#send message



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, msg):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = self.client.messages.create(from_=SENDER_NUM, to=RECEIVER_NUM, body= msg)
        