from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = '4b1a14e3aa52443ae8fd9084e80b6412'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    cities = request.args.get('cities')

    if not cities:
        return jsonify({'error': 'Cities parameter is required'}), 400
    
    city_list = cities.split(',')

    all_weather_data = []

    for city in city_list:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric',
        }


        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                date_time_utc = datetime.utcfromtimestamp(data['dt'])
                precipitation = 0.0
                if 'rain' in data and '1h' in data['rain']:
                    precipitation = data['rain']['1h']
                elif 'snow' in data and '1h' in data['snow']:
                    precipitation = data['snow']['1h']
                weather = {
                    'City': data['name'],
                    'Temperature': data['main']['temp'],
                    'Description': data['weather'][0]['description'],
                    'Maximum_Temperature': data['main']['temp_max'],
                    'Mininum_Temperature': data['main']['temp_min'],
                    'Wind_Speed': data['wind']['speed'],
                    'Humidity': data['main']['humidity'],
                    'Pressure': data['main']['pressure'],
                    'Date': date_time_utc.strftime('%Y-%b-%d'),
                    'Day': date_time_utc.strftime('%A'),              
                    'Precipitation': precipitation
                }
                all_weather_data.append(weather)


            else:

                error_message = data.get('message', 'Unknown error')
                return jsonify({'error': f'Failed to get weather data. {error_message}'}), response.status_code

        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500

    return jsonify(all_weather_data)

if __name__ == '__main__':
    app.run(debug=True)
