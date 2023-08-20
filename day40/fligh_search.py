from data_manager import DataManager
from flight_data import FlightData
from email_sender import SendEmail


# default destination airports written here , these are also included in the sheet 
# if you want to add more or update their prices please look at data_manager module
AIRPORT_CODES = {
    "Paris":"PAR",
    #"Berlin":"BER",
    #"Tokyo":"TYO",
    #"Sydney":"SYD",
    #"Istanbul":"IST",
    #"Kuala Lumpur":"KUL",
    #"New York":"JFK    ",
    #"San Francisco": "SFO",
    #"Cape Town":"CPT",
}

class FlightSearch:
    """
    This class is responsible for looking for cheaper prices than average ones in sheets
    """
    def __init__(self, flightData = FlightData()):
        self.data_manager = DataManager()
        self.flight_data = flightData
     

    def searchCheapFlights(self, from_airport = "IST"):
        for city in AIRPORT_CODES:
            to_airport = AIRPORT_CODES[city]
            flightData = self.flight_data.getFlightData(from_airport, to_airport)
            current_total_price = float(self.flightData[1]['price']['total'])
        
            # some additional info to inform user
            num_bookable_seats = flightData[1]['numberOfBookableSeats']
            lastTicketingDateTime = flightData[1]['lastTicketingDateTime']
            if current_total_price < self.data_manager.getLowestPrice(city_name=city):
                # print("A cheap flight detected, Get Quickkk")
                # print(f"From {from_airport} to {city} are available for only {current_total_price}$")
                # print(f"Last Date to book a seat{lastTicketingDateTime}")
                # print(f"{num_bookable_seats} seats are available")
                # #message body
                message_body = 'Headline: ' +"A cheaper Flight Ticket Found Get Quickk" + '\n' \
                                + 'Brief: ' + f"From IST to {city} are available for only {current_total_price}$" \
                                + f"Last Date to book a seat{lastTicketingDateTime}" \
                                + f"{num_bookable_seats} seats are available"
                # notify saved users
                email_sender = SendEmail()
                email_sender.sendEmail(message_to_send= message_body)   


            else:
                print("Nothing to report")
