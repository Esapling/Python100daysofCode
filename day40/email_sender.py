import smtplib, os
from data_manager import DataManager

# an example data returned from the getUsers method
# [{'name': 'Enes Fidan', 'email': 'enesfidan92@gmail.com', 'id': 2}]


class SendEmail:
    def __init__(self):
        self.sender = os.environ['EMAIL_USER='] # chage this to your own will
        self.sender_password = os.environ["EMAIL_PASS"] # your email password or a special pass given by your email for 3rd party apps
        data_manager = DataManager()
        self.users = data_manager.getUsers()

    def sendEmail(self, message_to_send):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()   #transport layer security , message encrypted
            if self.users == None:
                return 
            for user in self.users:
                connection.login(user=self.sender, password= self.sender_password)
                connection.sendmail(from_addr=self.sender, to_addrs=user , msg=f"Subject: Come QUICKKK\n\n{message_to_send}")
                print(f"Email successfully sended to the user {user['name']}")
