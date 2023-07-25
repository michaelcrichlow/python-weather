from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# this loads the environment variable
load_dotenv()


def get_current_weather(city="Buena Park"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=imperial"
    weather_data_as_json = requests.get(request_url).json()

    return weather_data_as_json


def main() -> None:
    city = input("Enter a city: ")
    city = city.strip()     # remove whitespace
    if city == "":
        city = "Buena Park"

    weather_data = get_current_weather(city)
    pprint(weather_data)


if __name__ == '__main__':
    main()
