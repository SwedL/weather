import datetime
import string
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

import numpy as np
from django.core.cache import cache

from ..repositories.forecast import ForeCastRepository


@dataclass
class ForeCastService:
    forecast_repository: ForeCastRepository = field(init=False, default=ForeCastRepository())

    @property
    def weekday(self):
        """ Функция возвращает список дней недели """
        return [date.today() + timedelta(days=i) for i in range(7)]

    def get_weather_forecast_in_city(self, city_name: str) -> list[Day]:
        """ Функция возвращает список объектов класса Day на неделю, из кэша или через API запросы. """
        if date_and_temperature_list := cache.get(city_name):
            return date_and_temperature_list
        else:
            return self.get_latest_weather_forecast_in_city(city_name)

    def get_latest_weather_forecast_in_city(self, city_name: str) -> list[Day]:
        """
        Функция получает название города, находит его координаты,
        затем по координатам получает данные температур на неделю.
        Возвращает список экземпляров Day (дата, температура) каждого дня недели.
        """
        language = 'en' if all(map(lambda s: s in string.ascii_letters, city_name.lower())) else 'ru'
        try:
            # получаем данные города из списка городов подходящих под заданное имя
            city = self.forecast_repository.find_city(city_name=city_name, language=language)['results'][0]

            # получаем данные погоды по координатам города
            city_temperature_data = self.forecast_repository.get_temperature_by_geo_coord(
                latitude=city['latitude'],
                longitude=city['longitude'],
                hourly='temperature_2m',
            )
        except Exception as err:
            raise err

        max_temperature_by_day_week = self.proceed_temperature_data(city_temperature_data)
        date_and_temperature_list = self.create_date_and_temperature_list(max_temperature_by_day_week)
        cache.set(city_name, date_and_temperature_list, 3600)

        return date_and_temperature_list

    @staticmethod
    def proceed_temperature_data(city_temperature_data: dict[str, Any]):
        all_temperatures_list = city_temperature_data['hourly']['temperature_2m']  # выбираем температуры на неделю
        temperature_by_day_week = np.reshape(all_temperatures_list, (7, 24)).tolist()  # группируем температуры по дням
        return [max(t) for t in temperature_by_day_week]

    def create_date_and_temperature_list(self, temperatures_by_week: list[str] = None):
        if temperatures_by_week is None:
            temperatures_by_week = ['-'] * 7
        return [Day(d, t) for d, t in zip(self.weekday, temperatures_by_week)]


@dataclass
class Day:
    date: datetime.date
    temperature: str
