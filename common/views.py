from typing import Dict, List
import requests
from transliterate import translit


class WeatherSource:
    URL_GET_COORD = "https://geocoding-api.open-meteo.com/v1/search"
    URL_WEATHER_FORECAST = "https://api.open-meteo.com/v1/forecast"

    def get_weather_forecast(self, city):
        # Транслитерация названия города с русского на английский
        city_en = translit(city, language_code='ru', reversed=True)
        all_cities_data = requests.get(url=self.URL_GET_COORD, params={'name': city_en})
        data_first_city = all_cities_data.json()['results'][0]
        params = {
            'latitude': data_first_city['latitude'],
            'longitude': data_first_city['longitude'],
            'hourly': 'temperature_2m',
        }

        response = requests.get(url=self.URL_WEATHER_FORECAST, params=params)
        return response.json()
