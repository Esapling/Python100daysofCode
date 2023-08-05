data = {
  "prices": [
    {
      "city": "Paris", "PAR"
      "iataCode": "",
      "lowestPrice": 54,
      "id": 2
    },
    {
      "city": "Berlin","BER"
      "iataCode": "",
      "lowestPrice": 42,
      "id": 3
    },
    {
      "city": "Tokyo","TYO"
      "iataCode": "",
      "lowestPrice": 485,
      "id": 4
    },
    {
      "city": "Sydney","SYD"
      "iataCode": "",
      "lowestPrice": 551,
      "id": 5
    },
    {
      "city": "Istanbul","IST"
      "iataCode": "",
      "lowestPrice": 95,
      "id": 6
    },
    {
      "city": "Kuala Lumpur","KUL"
      "iataCode": "",
      "lowestPrice": 414,
      "id": 7
    },
    {
      "city": "New York","JFK"
      "iataCode": "",
      "lowestPrice": 240,
      "id": 8
    },
    {
      "city": "San Francisco", "SFO"
      "iataCode": "",
      "lowestPrice": 260,
      "id": 9
    },
    {
      "city": "Cape Town", "CPT"
      "iataCode": "",
      "lowestPrice": 378,
      "id": 10
    }
  ]
}
AIRPORT_CODES = {
    "Paris":"PAR",
    "Berlin":"BER",
    "Tokyo":"TYO",
    "Sydney":"SYD",
    "Istanbul":"IST",
    "Kuala Lumpur":"KUL",
    "New York":"JFK",
    "San Francisco": "SFO",
    "Cape Town":"CPT",
}

for city in AIRPORT_CODES:
    print(AIRPORT_CODES[city])