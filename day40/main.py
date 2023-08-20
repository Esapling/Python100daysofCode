from flight_data import FlightData
from fligh_search import FlightSearch

def main():
    m_flightData = FlightData()
    m_flightSearch = FlightSearch(m_flightData)
    m_flightSearch.searchCheapFlights()


if __name__ == '__main__':
    main()
