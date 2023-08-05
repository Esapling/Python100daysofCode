import requests, os
from data_manager import DataManager
from datetime import date
from dateutil.relativedelta import relativedelta
from notification_manager import NotificationManager


# add your airport code here
AIRPORT_CODES = {
    "Paris":"PAR",
    #"Berlin":"BER",
    #"Tokyo":"TYO",
    #"Sydney":"SYD",
    #"Istanbul":"IST",
    #"Kuala Lumpur":"KUL",
    #"New York":"JFK",
    #"San Francisco": "SFO",
    #"Cape Town":"CPT",
}

m_airport_code = "PAR"

#first we need to get our auth token using a post request (api requirement)

m_api_key = os.environ['AUTH_AMEDEUS_KEY']
m_api_secret = os.environ['AUTH_AMEDEUS_SECRET']

api_auth = "https://test.api.amadeus.com/v1/security/oauth2/token"

payload = {
    "grant_type": "client_credentials",
    "client_id": m_api_key,
    "client_secret": m_api_secret
}
header_token = {
    "Content-Type": "application/x-www-form-urlencoded"
}

auth_token_response = requests.post(url=api_auth, headers=header_token, data=payload)
auth_token_response.raise_for_status()

#response data is a json data includes some authentication info and our token that we need to pass our main api to get flight data

#note that this token is persisten i.e it will expire in some seconds 
# so you must take it as a variable 
# dont try to save it as a const like your auth
my_token = auth_token_response.json()['access_token']



#--------------------------------------------GETTING FLIGHT DATA USING POST REQUEST---------------------------#

# Get today's date
today = date.today()

# our app will be looking for cheap flights for 1 month later than today 
one_month_later = today + relativedelta(months=1)



params_flightData = {
    "originLocationCode": "IST", #Required
    "destinationLocationCode":m_airport_code ,#Required
    "departureDate": one_month_later, #Required
    "adults":1,#Required
    "currencyCode":"USD", #Optional
    #"max":1, 
}
header_flightData = {
    "Authorization": f"Bearer {my_token}"
}   


api_flightData = "https://test.api.amadeus.com/v2/shopping/flight-offers"




for city in AIRPORT_CODES:
    m_airport_code = AIRPORT_CODES[city]

    flight_response = requests.get(url=api_flightData, params=params_flightData, headers=header_flightData)
    flight_response.raise_for_status()
    
    flightData = flight_response.json()['data']

    #instantiate data manager object to get your lowest prices 
    data_manager = DataManager()
    
    current_total_price =float(flightData[1]['price']['total'])
    # some additional info to acknowledge user
    num_bookable_seats = flightData[1]['numberOfBookableSeats']
    lastTicketingDateTime = flightData[1]['lastTicketingDateTime']


    if current_total_price < data_manager.getLowestPrice(city_name=city):
        print("A cheap flight detected, Get Quickkk")
        print(f"From IST to {city} are available for only {current_total_price}$")
        print(f"Last Date to book a seat{lastTicketingDateTime}")
        print(f"{num_bookable_seats} seats are available")

        #message body
        message_body = 'Headline: ' +"A cheaper Flight Ticket Found Get Quickk" + '\n' \
                        + 'Brief: ' + f"From IST to {city} are available for only {current_total_price}$" \
                        + f"Last Date to book a seat{lastTicketingDateTime}" \
                        + f"{num_bookable_seats} seats are available"
        
        
        notify = NotificationManager(msg=message_body) # send a msg 
    else:
        print("Nothing to report")

class FlightData:
    #This class is responsible for structuring the flight data.
    pass