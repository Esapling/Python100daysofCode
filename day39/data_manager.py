import requests, os
from requests.auth import HTTPBasicAuth



MAX_INT = 10000000
sheety_user_name ="98869ea06301cb318c558a37a93f2d52"
#for each project in sheety you need to set up your authentication settings 
#following keys will not be the same as before if you dont set them as they were
m_user_name = os.environ['AUTH_SHEETY_USER_NAME']
m_password = os.environ['AUTH_SHEETY_PASSWORD']
m_authenticate = HTTPBasicAuth(username=m_user_name, password=m_password)
project_name = "flightDeals"
sheet_name = "prices"
sheety_end_point = f"https://api.sheety.co/{sheety_user_name}/{project_name}/{sheet_name}"


class DataManager:
    def __init__(self):
        response = requests.get(url=sheety_end_point, auth=m_authenticate)
        response.raise_for_status() # if request fails then raise an error
        self.data = response.json()

    def getLowestPrice(self, city_name):
        cities = self.data['prices']
        for city in cities:
            if city['city'] == city_name.title():
                return city['lowestPrice']
                
        return MAX_INT # return something big so that no changes can be applicable
    
# trial = DataManager()
# lp = trial.getLowestPrice("Istanbul")
# print(lp)
