In this project it is aimed to create an application that looks for cheaper flight prices and informs its users when one or more are found via email.
the application uses Amadeus API for searching for current flight prices and additional information. As for average prices, the app gets these prices from a google sheet using Sheety api.It is kindly requested for a user to write manually base prices for a locaation to other locations.Here by default , our database includes prices from Istanbul (IST) to other location and also 'IST' is given as a default value to a parameter in searchCheapFlights method in fight_search module. Please change this value to your database default locataion wherever you take as a departure place.
Or you might get tricky notifications :) .
You can also use setNewHeading() method in data_manager module to add new cities with base prices to your data sheet.

Our data sheet has another sheet which has users' info whom our application will send emails if it finds cheaper flights.You can add, update your users from the data_manager module . 

While sending different requests to any api needs to take care of exceptions carefully because any requst might rise a relevant error in order for our application works without any crashes we need to handle them.

To send email our application uses smtplib module (please see for more information https://docs.python.org/3/library/smtplib.html)

This is an example row of two sheet pages , you can also set your sheets like this to use the app in the same way.

1-)    prices sheet
    example sheet structure
City	IATA Code	Lowest Price
Paris	PAR	        54
2-)
    users sheet
    Name	Email	
Enes Fidan	example_gmail_address@gmail.com	


Or you can design it in your own will but do not forget to update the code's relevant parts that handle the api , and also Sheety api uses camelCase style. So if you have a Iata Code row then you can reach it from your code 'iataCode' string. 

Lastly if you want your application to run every time and send you emails when it finds good deals, you can load your application to a cloud and make it work in there. To do this please look at https://www.pythonanywhere.com/


For more information: 
https://sheety.co/
https://developers.amadeus.com/
https://docs.python.org/3/library/smtplib.html
https://www.pythonanywhere.com/
