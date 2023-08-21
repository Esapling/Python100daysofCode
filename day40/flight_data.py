import requests, os
from data_manager import DataManager
from datetime import date
from dateutil.relativedelta import relativedelta
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

#for more information about Amedeus api and more please visit --> https://developers.amadeus.com/self-service/category/flights

class FlightData:
    def __init__(self):
        # set some constants
        m_api_key = os.environ['AUTH_AMEDEUS_KEY']
        m_api_secret = os.environ['AUTH_AMEDEUS_SECRET']
        self.api_auth = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.payload = {
            "grant_type": "client_credentials",
            "client_id": m_api_key,
            "client_secret": m_api_secret
        }
        self.header_token = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.api_flightData = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.my_token  = None


    
    def getFlightData(self, location_code , destionation_code):
        """
        For each call , the method gets a new token by an api request and returns flight data 
        """
        # Get today's date
        today = date.today()
        print("A")
        # our app will be looking for cheap flights for 1 month later than today 
        one_month_later = today + relativedelta(months=1)
        #first we need to get our auth token using a post request (api requirement)
        flightData = None 
        try:
            self.getToken()
            print("CS")
        except HTTPError as token_error:
            print(f"HTTP Error: {token_error}")
        except ConnectionError as conn_error:
            print(f"Connection Error: {conn_error}")
        except Timeout as timeout_error:
            print(f"Timeout Error: {timeout_error}")
        except RequestException as req_error:
            print(f"Request Exception: {req_error}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            #if token successfuly created
            #headers
            self.header_flightData = {
                "Authorization": f"Bearer {self.my_token}"
            }   
            #parameters
            params_flightData = {
                "originLocationCode": location_code, #Required
                "destinationLocationCode": destionation_code ,#Required
                "departureDate": one_month_later, #Required
                "adults":1,#Required
                "currencyCode":"USD", #Optional
            }
            flight_response = requests.get(url=self.api_flightData, params=params_flightData, headers=self.header_flightData)
            flight_response.raise_for_status()
            flightData = flight_response.json()['data']
            print("D")
        finally:
            return flightData
        
        
    def getToken(self):
        auth_token_response = requests.post(url=self.api_auth, headers=self.header_token, data=self.payload)
        auth_token_response.raise_for_status()
        #response is a json data that includes some authentication info and our token that we need 
        #to pass our main api to get flight data

        #note that this token is persisten i.e it will expire in some seconds 
        # so you must take it as a variable  and update it for each data call
        # dont try to save it as a const
        self.my_token = auth_token_response.json()['access_token']

        
        

