# Backend-Weather-API
Weather API using Flask

This is a simple Flask application that provides weather information for multiple cities using the OpenWeatherMap API.

PROCEDURE:

1. Install dependencies such as flask, datetime, and other required libraries.
2. Obtain an API key from OpenWeatherMap and use it in the file.
3. Run the application
4. Open Postman and create a new request to http://127.0.0.1:5000/weather with the GET method.
5. Add a query parameter location with the value being the city.
6. Send the request and check the output.

EXPLANATION:

1. Run the python script on VScode
2. In the terminal you can see the base url http://127.0.0.1:5000 . When you click on this url, you will see 404 error.
3. Now go to your Postman workspace, set the request type to GET
4. Enter the URL for your Flask API endpoint i.e, http://127.0.0.1:5000/weather?.
5. Click on the "Params" tab. In the "Key" column, enter location . In the "Value" column, enter the city and state for which you want to retrieve the weather information.
6. Click the send button to make the request.
7. Now go back to the base url, in-order to fetch the weather data, you have to append the base url with the api endpoint i.e, http://127.0.0.1:5000/weather?cities (eg: http://127.0.0.1:5000/weather?cities=bengaluru,mumbai,london).
8. Now you can see the json file.

ENDPOINTS:

Get Weather Information
Endpoint: /weather
Method: GET
Parameters:
cities: Comma-separated list of city names.

RESPONSE:
The API will return a JSON object containing weather information for each requested city. The data includes:

City name
Temperature (in Celsius)
Weather description
Maximum temperature
Minimum temperature
Wind speed
Humidity
Pressure
Date (in UTC)
Day of the week
Precipitation (rain or snow in the last 1 hour, if any)

ERROR HANDLING
If there are any errors, the API will return a JSON object with an error message and the appropriate HTTP status code.

ADDITIONALS: 
1. This python script accepts multiple query parameters. The code includes the ability to retrieve weather information for multiple locations through the /weather endpoint.
2. The code includes try-except blocks to catch and handle exceptions that may occur during API requests or data processing.
3. Appropriate status codes are returned in the API responses, such as 400 for bad requests, 200 for response and 500 for internal server errors.

SCREENSHOTS:

Weather API using Flask

This is a simple Flask application that provides weather information for multiple cities using the OpenWeatherMap API.

PROCEDURE:

1. Install dependencies such as flask, datetime, and other required libraries.
2. Obtain an API key from OpenWeatherMap and use it in the file.
3. Run the application
4. Open Postman and create a new request to http://127.0.0.1:5000/weather with the GET method.
5. Add a query parameter location with the value being the city.
6. Send the request and check the output.

EXPLANATION:

1. Run the python script on VScode
2. In the terminal you can see the base url http://127.0.0.1:5000 . When you click on this url, you will see 404 error.
3. Now go to your Postman workspace, set the request type to GET
4. Enter the URL for your Flask API endpoint i.e, http://127.0.0.1:5000/weather?.
5. Click on the "Params" tab. In the "Key" column, enter location . In the "Value" column, enter the city and state for which you want to retrieve the weather information.
6. Click the send button to make the request.
7. Now go back to the base url, in-order to fetch the weather data, you have to append the base url with the api endpoint i.e, http://127.0.0.1:5000/weather?cities (eg: http://127.0.0.1:5000/weather?cities=bengaluru,mumbai,london).
8. Now you can see the json file.

ENDPOINTS:

Get Weather Information
Endpoint: /weather
Method: GET
Parameters:
cities: Comma-separated list of city names.

RESPONSE:
The API will return a JSON object containing weather information for each requested city. The data includes:

City name
Temperature (in Celsius)
Weather description
Maximum temperature
Minimum temperature
Wind speed
Humidity
Pressure
Date (in UTC)
Day of the week
Precipitation (rain or snow in the last 1 hour, if any)

ERROR HANDLING
If there are any errors, the API will return a JSON object with an error message and the appropriate HTTP status code.

ADDITIONALS: 
1. This python script accepts multiple query parameters. The code includes the ability to retrieve weather information for multiple locations through the /weather endpoint.
2. The code includes try-except blocks to catch and handle exceptions that may occur during API requests or data processing.
3. Appropriate status codes are returned in the API responses, such as 400 for bad requests, 200 for response and 500 for internal server errors.

SCREENSHOTS:
<img width="1464" alt="Screenshot 2023-11-25 at 5 32 27 PM" src="https://github.com/Sejal84/Backend-Weather-API/assets/150245903/2507dd2e-6201-44f8-a9d8-6652a1ccd457">

<img width="1464" alt="Screenshot 2023-11-25 at 5 31 56 PM" src="https://github.com/Sejal84/Backend-Weather-API/assets/150245903/72cd0305-d4a8-4c1d-aa98-519f9d16f6bc">

