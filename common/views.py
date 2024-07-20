import string
from typing import Dict, Tuple

import numpy as np
import requests


class WeatherSource:
    """Класс получения прогноза погоды по городу"""
    URL_GET_COORD = "https://geocoding-api.open-meteo.com/v1/search"
    URL_WEATHER_FORECAST = "https://api.open-meteo.com/v1/forecast"

    def get_data_all_cities(self, params: Dict) -> Dict:
        """ Функция делает запрос и возвращает данные по всем городам, подходящих под заданное имя города """
        return requests.get(url=self.URL_GET_COORD, params=params, timeout=3).json()

    def get_city_temperature_data(self, params: Dict) -> Dict:
        """ Функция делает запрос и возвращает данные температур на неделю по заданным координатам"""
        return requests.get(url=self.URL_WEATHER_FORECAST, params=params, timeout=3).json()

    def get_weather_forecast(self, city: str) -> Tuple:
        """
        Функция получает название города, находит его координаты, затем по координатам получает данные
        по температурам этих координат на неделю.
        Возвращает список из максимальных температур каждого дня недели.
        """
        if all(map(lambda s: s in string.ascii_letters, city.lower())):
            params = {'name': city, 'language': 'en'}
        else:
            params = {'name': city, 'language': 'ru'}

        # получаем данные по всем городам, подходящих под заданное имя города
        data_all_cities = self.get_data_all_cities(params=params)

        # Если координаты города не были получены, возвращается пустой список и флаг ошибки
        if data_all_cities.get('results', None) is None:
            return ['-' for _ in range(7)], 'error'

        data_first_city = data_all_cities['results'][0]  # получаем данные из наиболее точного указания города
        params = {
            'latitude': data_first_city['latitude'],
            'longitude': data_first_city['longitude'],
            'hourly': 'temperature_2m',
        }

        city_temperature_data = self.get_city_temperature_data(params=params)  # получаем данные по городу
        all_temperatures_list = city_temperature_data['hourly']['temperature_2m']  # выбираем температуры на неделю
        temperature_by_day_week = np.reshape(all_temperatures_list, (7, 24)).tolist()  # группируем температуры по дням
        max_temperature_by_day_week = [max(t) for t in temperature_by_day_week]  # создаём список максимальных температур на неделю

        return max_temperature_by_day_week, None
