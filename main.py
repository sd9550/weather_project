import requests
import os

WEATHER_ENDPOINT = "http://api.weatherstack.com/forecast"
API_KEY = os.environ["API_KEY"]

user_entry = input("Enter a city to see the current weather forecast: ")

params = {
    "access_key": API_KEY,
    "query": user_entry,
    "units": "f"
}

try:
    response = requests.get(url=WEATHER_ENDPOINT, params=params)
    response.raise_for_status()

    weather_data = response.json()
    current_city = weather_data["location"]["name"]
    current_temp = weather_data["current"]["temperature"]
    current_desc = weather_data["current"]["weather_descriptions"][0].lower()

    print(f"The current temperature in {current_city} is {current_temp} degrees and it is {current_desc}.")
except KeyError as e:
    print(f"Error: {e}")
