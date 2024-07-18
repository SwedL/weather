from typing import Dict, List, Tuple
import requests
from transliterate import translit
import numpy as np


class WeatherSource:
    """Класс получения прогноза погоды по городу"""
    URL_GET_COORD = "https://geocoding-api.open-meteo.com/v1/search"
    URL_WEATHER_FORECAST = "https://api.open-meteo.com/v1/forecast"

    def get_weather_forecast(self, city) -> Tuple:
        """Функция """
        # Транслитерация названия города с русского на английский
        city_en = translit(city, language_code='ru', reversed=True)
        all_cities_data = requests.get(url=self.URL_GET_COORD, params={'name': city_en})

        if all_cities_data.json().get('results', None) is None:
            return ['-' for _ in range(7)], 'error'

        data_first_city = all_cities_data.json()['results'][0]  # получаем данные из наиболее точного указания города
        params = {
            'latitude': data_first_city['latitude'],
            'longitude': data_first_city['longitude'],
            'hourly': 'temperature_2m',
        }

        all_data_city = requests.get(url=self.URL_WEATHER_FORECAST, params=params)  # получаем данные по городу
        all_temperatures_list = all_data_city.json()['hourly']['temperature_2m']  # выбираем температуры на неделю
        temperature_by_day_week = np.reshape(all_temperatures_list, (7, 24)).tolist()  # группируем температуры по дням
        max_temperature_by_day_week = [max(t) for t in temperature_by_day_week]  # создаём список максимальных температур на неделю

        return max_temperature_by_day_week, None
