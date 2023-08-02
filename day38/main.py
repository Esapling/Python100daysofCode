import requests , os , datetime
from requests.auth import HTTPBasicAuth

#---------------------------------DEFINING SOME CONSTANTS-----------------------#
MY_APP_ID = os.environ['NUTRITIONIX_APP_ID']
MY_APP_KEY = os.environ['NUTRITIONIX_APP_KEY']
SHEETY_USERNAME = "98869ea06301cb318c558a37a93f2d52"
SHEETY_PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"

user_name_sheety = os.environ['SHEETY_USER_NAME']
pass_sheety = os.environ['SHEETY_PASSWORD']



sheety_auth = HTTPBasicAuth(username=user_name_sheety, password=pass_sheety)

#----------------------------------APIs------------------------#

sheety_end_point = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEET_NAME}"
post_endpoint = "/v2/natural/exercise"
url ="https://trackapi.nutritionix.com"

user_input = input("Tell me which exercise you did? ")

#----------------SETTING UP NUTRITIONIX API AND SENDING A POST REQUEST----------------#

"""
- x-app-id: Your app ID issued from developer.nutritionix.com)
- x-app-key: Your app key issued from developer.nutritionix.com)
- x-remote-user-id:  A unique identifier to represent the end-user who is accessing the Nutritionix API.
If in development mode, set this to 0.  This is used for billing purposes to determine the number of active users your app has.
"""

m_headers_nutritionix = {
    "x-app-id":MY_APP_ID,
    "x-app-key":MY_APP_KEY,
    "x-remote-user-id":"0",
}

body_nutritionix = {
    "query":user_input,
    "gender":"male",
    "weight_kg":70,
    "height_cm":180,
    "age":25
}
exercise_response = requests.post(url=url+post_endpoint, headers=m_headers_nutritionix, json=body_nutritionix)

exercise_info = exercise_response.json()

print(exercise_response.text)
#----------------SETTING UP SHEETY API AND SENDING A POST REQUEST----------------#

date = str(datetime.datetime.now()).split(' ')
today = date[0] # the first one is the date and the second one is time 
time = date[1] # to ignore seconds 


total_time_spent = exercise_info['exercises'][0]['duration_min']
calories_gone  = exercise_info['exercises'][0]['nf_calories']
exercise_type = exercise_info['exercises'][0]['name']




data_to_put_rows_in_sheety = {
    "workout": 
        {   
            "date":today,
            "time":time,
            "exercise":exercise_type.title(),
            "duration":total_time_spent,
            "calories":calories_gone
        }
}
headers_sheety = {
    "Content-Type": "application/json"
}



sheety_response = requests.post(url=sheety_end_point, json=data_to_put_rows_in_sheety, headers=headers_sheety, auth=sheety_auth)
sheety_response.raise_for_status()