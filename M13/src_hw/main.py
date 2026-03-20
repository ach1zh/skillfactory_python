# main.py
import requests

def get_weather(api_key, city):
    
    base_url = "http://api.weatherstack.com/current"
    
    params = {
        'access_key': api_key,
        'query': city
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data['current']['temperature'], weather_data['current']['weather_descriptions'][0]
    else:
        raise Exception("Error while fetching weather data")
