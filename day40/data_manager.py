import requests, os
from requests.auth import HTTPBasicAuth
""" 
    example sheet structure
City	IATA Code	Lowest Price
Paris	PAR	        54
"""


class DataManager(Exception):
    """
    This class manages average flight prices and users' info on google sheets
    """
    def __init__(self):
        super().__init__()
        self.sheety_user_name =os.environ['SHEETY_USER_NAME']
        #for each project in sheety you need to set up your authentication settings 
        #following keys will not be the same as before if you dont set them as they were
        auth_user_name = os.environ['AUTH_SHEETY_USER_NAME']
        auth_password = os.environ['AUTH_SHEETY_PASSWORD']
        self.authenticate = HTTPBasicAuth(username=auth_user_name, password=auth_password)
        self.project_name = "flightDeals"
    
    def getIATACode(self, city_name):
        sheet_name = "prices"
        sheety_end_point = f"https://api.sheety.co/{self.sheety_user_name}/{self.project_name}/{sheet_name}"
        response = requests.get(url=sheety_end_point, auth=self.authenticate)
        response.raise_for_status() # if request fails then raise an error
        self.data = response.json()
        for row in self.data['prices']:
            if row['city'] == city_name.title():
                return row['iataCode']
        raise DataManager(f"No match found for city {city_name}")

    def searchLowestPrice(self,city_name):
        sheet_name = "prices"
        sheety_end_point = f"https://api.sheety.co/{self.sheety_user_name}/{self.project_name}/{sheet_name}"
        response = requests.get(url=sheety_end_point, auth=self.authenticate)
        response.raise_for_status() # if request fails then raise an error
        self.data = response.json()
        for row in self.data['prices']:
            if row['city'] == city_name.title():
                return row['lowestPrice']
        raise DataManager(f"No match found for city {city_name}")


    def getLowestPrice(self, city_name):
        try:
            lowest_price = self.searchLowestPrice(city_name)
        except DataManager as custom_error:
            print(f"{custom_error}")
            lowest_price = -1 # return -1 so notification will be made

        return lowest_price

    def addUserToSheet(self, user):
        sheet_name = "users"
        sheety_end_point = f"https://api.sheety.co/{self.sheety_user_name}/{self.project_name}/{sheet_name}"
        #https://api.sheety.co/98869ea06301cb318c558a37a93f2d52/flightDeals/users
        headers_sheety = {  
            "Content-Type": "application/json"
        }
        row_body  ={
            "user" : {
                "name": user['name'],
                "email": user['email'],
            }
        }
        post_response = requests.post(url=sheety_end_point, auth=self.authenticate, json=row_body, headers=headers_sheety)
        #note: here the true parameter for data is 'json' not 'data'
        post_response.raise_for_status()
        print("You have been successfully registered, Cheap Flightss")


    def updatePrice(self,city_name, new_price):
        sheet_name = "prices"
        object_id = 0
        sheety_end_point = f"https://api.sheety.co/{self.sheety_user_name}/{self.project_name}/{sheet_name}"
        response = requests.get(url=sheety_end_point, auth=self.authenticate)
        response.raise_for_status() # if request fails then raise an error
        self.data = response.json()
        for row in self.data['prices']:
            if row['city'] == city_name.title():
                object_id = row['id']
                old_iataCode = row['iataCode']
        api_put_url = f"https://api.sheety.co/{self.sheety_user_name}/{self.project_name}/{sheet_name}/{object_id}"

        new_row = {
            "price":{
                "city": city_name,
                "iataCode": old_iataCode,
                "lowestPrice": new_price
            }
        }
        response_put = requests.put(url=api_put_url, auth=self.authenticate, json=new_row)
        response_put.raise_for_status()
        print("successfully updated")

    def getUsers(self):
        sheet_name = "users"
        sheety_end_point = f"https://api.sheety.co/{self.sheety_user_name}/{self.project_name}/{sheet_name}"
        response = requests.get(url=sheety_end_point, auth=self.authenticate)
        response.raise_for_status() # if request fails then raise an error
        self.data = response.json()
        return self.data['users']    
    
