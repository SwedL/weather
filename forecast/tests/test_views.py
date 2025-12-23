import unittest
from http import HTTPStatus
from unittest.mock import patch

from django.test import SimpleTestCase
from django.urls import reverse

from forecast.forms import CityNameForm
from forecast.repositories.forecast import ForeCastRepository
from forecast.services.forecast import Day, ForeCastService

mock_value_moscow = {"results": [
    {"id": 524901, "name": "Moscow", "latitude": 55.75222, "longitude": 37.61556, "elevation": 144.0,
     "feature_code": "PPLC", "country_code": "RU", "admin1_id": 524894, "timezone": "Europe/Moscow",
     "population": 10381222, "country_id": 2017370, "country": "Russia", "admin1": "Moscow"},
    {"id": 5601538, "name": "Moscow", "latitude": 46.73239, "longitude": -117.00017, "elevation": 786.0,
     "feature_code": "PPLA2", "country_code": "US", "admin1_id": 5596512, "admin2_id": 5598264,
     "timezone": "America/Los_Angeles", "population": 25060, "postcodes": ["83843", "83844"], "country_id": 6252001,
     "country": "United States", "admin1": "Idaho", "admin2": "Latah"},
    {"id": 5202009, "name": "Moscow", "latitude": 41.33675, "longitude": -75.51852, "elevation": 476.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 6254927, "admin2_id": 5196674, "admin3_id": 5202011,
     "timezone": "America/New_York", "population": 1960, "postcodes": ["18444"], "country_id": 6252001,
     "country": "United States", "admin1": "Pennsylvania", "admin2": "Lackawanna", "admin3": "Borough of Moscow"},
    {"id": 5151660, "name": "Dalton", "latitude": 40.79894, "longitude": -81.69541, "elevation": 336.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 5165418, "admin2_id": 5175898, "admin3_id": 5173320,
     "timezone": "America/New_York", "population": 1850, "postcodes": ["44618"], "country_id": 6252001,
     "country": "United States", "admin1": "Ohio", "admin2": "Wayne", "admin3": "Sugar Creek Township"},
    {"id": 4642988, "name": "Moscow", "latitude": 35.06203, "longitude": -89.40396, "elevation": 108.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 4662168, "admin2_id": 4621908,
     "timezone": "America/Chicago", "population": 532, "postcodes": ["38057"], "country_id": 6252001,
     "country": "United States", "admin1": "Tennessee", "admin2": "Fayette"},
    {"id": 5124210, "name": "Leicester", "latitude": 42.77201, "longitude": -77.89667, "elevation": 198.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 5128638, "admin2_id": 5124928, "admin3_id": 5124211,
     "timezone": "America/New_York", "population": 455, "postcodes": ["14481"], "country_id": 6252001,
     "country": "United States", "admin1": "New York", "admin2": "Livingston", "admin3": "Town of Leicester"},
    {"id": 5446028, "name": "Moscow", "latitude": 37.32363, "longitude": -101.20572, "elevation": 930.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 4273857, "admin2_id": 5446576, "admin3_id": 5446032,
     "timezone": "America/Chicago", "population": 319, "postcodes": ["67952"], "country_id": 6252001,
     "country": "United States", "admin1": "Kansas", "admin2": "Stevens", "admin3": "Moscow Township"},
    {"id": 4518753, "name": "Moscow", "latitude": 38.85701, "longitude": -84.2291, "elevation": 152.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 5165418, "admin2_id": 4508924, "admin3_id": 4527700,
     "timezone": "America/New_York", "population": 186, "postcodes": ["45153"], "country_id": 6252001,
     "country": "United States", "admin1": "Ohio", "admin2": "Clermont", "admin3": "Washington Township"},
    {"id": 4122279, "name": "Moscow", "latitude": 34.14649, "longitude": -91.79513, "elevation": 59.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 4099753, "admin2_id": 4116433, "admin3_id": 4128344,
     "timezone": "America/Chicago", "postcodes": ["71659"], "country_id": 6252001, "country": "United States",
     "admin1": "Arkansas", "admin2": "Jefferson", "admin3": "Richland Township"},
    {"id": 4712467, "name": "Moscow", "latitude": 30.91325, "longitude": -94.82521, "elevation": 105.0,
     "feature_code": "PPL", "country_code": "US", "admin1_id": 4736286, "admin2_id": 4719903,
     "timezone": "America/Chicago", "postcodes": ["75960"], "country_id": 6252001, "country": "United States",
     "admin1": "Texas", "admin2": "Polk"}], "generationtime_ms": 0.3260374}

mock_value_city_temperature_data = {"latitude": 55.75, "longitude": 37.625, "generationtime_ms": 0.03695487976074219,
                                    "utc_offset_seconds": 0, "timezone": "GMT", "timezone_abbreviation": "GMT",
                                    "elevation": 141.0,
                                    "hourly_units": {"time": "iso8601", "temperature_2m": "°C"}, "hourly": {
        "time": ["2024-07-20T00:00", "2024-07-20T01:00", "2024-07-20T02:00", "2024-07-20T03:00", "2024-07-20T04:00",
                 "2024-07-20T05:00", "2024-07-20T06:00", "2024-07-20T07:00", "2024-07-20T08:00", "2024-07-20T09:00",
                 "2024-07-20T10:00", "2024-07-20T11:00", "2024-07-20T12:00", "2024-07-20T13:00", "2024-07-20T14:00",
                 "2024-07-20T15:00", "2024-07-20T16:00", "2024-07-20T17:00", "2024-07-20T18:00", "2024-07-20T19:00",
                 "2024-07-20T20:00", "2024-07-20T21:00", "2024-07-20T22:00", "2024-07-20T23:00", "2024-07-21T00:00",
                 "2024-07-21T01:00", "2024-07-21T02:00", "2024-07-21T03:00", "2024-07-21T04:00", "2024-07-21T05:00",
                 "2024-07-21T06:00", "2024-07-21T07:00", "2024-07-21T08:00", "2024-07-21T09:00", "2024-07-21T10:00",
                 "2024-07-21T11:00", "2024-07-21T12:00", "2024-07-21T13:00", "2024-07-21T14:00", "2024-07-21T15:00",
                 "2024-07-21T16:00", "2024-07-21T17:00", "2024-07-21T18:00", "2024-07-21T19:00", "2024-07-21T20:00",
                 "2024-07-21T21:00", "2024-07-21T22:00", "2024-07-21T23:00", "2024-07-22T00:00", "2024-07-22T01:00",
                 "2024-07-22T02:00", "2024-07-22T03:00", "2024-07-22T04:00", "2024-07-22T05:00", "2024-07-22T06:00",
                 "2024-07-22T07:00", "2024-07-22T08:00", "2024-07-22T09:00", "2024-07-22T10:00", "2024-07-22T11:00",
                 "2024-07-22T12:00", "2024-07-22T13:00", "2024-07-22T14:00", "2024-07-22T15:00", "2024-07-22T16:00",
                 "2024-07-22T17:00", "2024-07-22T18:00", "2024-07-22T19:00", "2024-07-22T20:00", "2024-07-22T21:00",
                 "2024-07-22T22:00", "2024-07-22T23:00", "2024-07-23T00:00", "2024-07-23T01:00", "2024-07-23T02:00",
                 "2024-07-23T03:00", "2024-07-23T04:00", "2024-07-23T05:00", "2024-07-23T06:00", "2024-07-23T07:00",
                 "2024-07-23T08:00", "2024-07-23T09:00", "2024-07-23T10:00", "2024-07-23T11:00", "2024-07-23T12:00",
                 "2024-07-23T13:00", "2024-07-23T14:00", "2024-07-23T15:00", "2024-07-23T16:00", "2024-07-23T17:00",
                 "2024-07-23T18:00", "2024-07-23T19:00", "2024-07-23T20:00", "2024-07-23T21:00", "2024-07-23T22:00",
                 "2024-07-23T23:00", "2024-07-24T00:00", "2024-07-24T01:00", "2024-07-24T02:00", "2024-07-24T03:00",
                 "2024-07-24T04:00", "2024-07-24T05:00", "2024-07-24T06:00", "2024-07-24T07:00", "2024-07-24T08:00",
                 "2024-07-24T09:00", "2024-07-24T10:00", "2024-07-24T11:00", "2024-07-24T12:00", "2024-07-24T13:00",
                 "2024-07-24T14:00", "2024-07-24T15:00", "2024-07-24T16:00", "2024-07-24T17:00", "2024-07-24T18:00",
                 "2024-07-24T19:00", "2024-07-24T20:00", "2024-07-24T21:00", "2024-07-24T22:00", "2024-07-24T23:00",
                 "2024-07-25T00:00", "2024-07-25T01:00", "2024-07-25T02:00", "2024-07-25T03:00", "2024-07-25T04:00",
                 "2024-07-25T05:00", "2024-07-25T06:00", "2024-07-25T07:00", "2024-07-25T08:00", "2024-07-25T09:00",
                 "2024-07-25T10:00", "2024-07-25T11:00", "2024-07-25T12:00", "2024-07-25T13:00", "2024-07-25T14:00",
                 "2024-07-25T15:00", "2024-07-25T16:00", "2024-07-25T17:00", "2024-07-25T18:00", "2024-07-25T19:00",
                 "2024-07-25T20:00", "2024-07-25T21:00", "2024-07-25T22:00", "2024-07-25T23:00", "2024-07-26T00:00",
                 "2024-07-26T01:00", "2024-07-26T02:00", "2024-07-26T03:00", "2024-07-26T04:00", "2024-07-26T05:00",
                 "2024-07-26T06:00", "2024-07-26T07:00", "2024-07-26T08:00", "2024-07-26T09:00", "2024-07-26T10:00",
                 "2024-07-26T11:00", "2024-07-26T12:00", "2024-07-26T13:00", "2024-07-26T14:00", "2024-07-26T15:00",
                 "2024-07-26T16:00", "2024-07-26T17:00", "2024-07-26T18:00", "2024-07-26T19:00", "2024-07-26T20:00",
                 "2024-07-26T21:00", "2024-07-26T22:00", "2024-07-26T23:00"],
        "temperature_2m": [17.7, 17.2, 16.9, 17.4, 18.7, 20.1, 21.5, 22.5, 23.2, 23.4, 23.2, 23.7, 23.6, 23.6, 22.9,
                           22.5, 21.4, 20.5, 19.6, 18.7, 18.0, 17.5, 17.0, 16.6, 16.2, 15.9, 15.9, 16.4, 17.4, 18.7,
                           20.1, 20.9, 21.3, 22.5, 23.0, 23.1, 23.2, 22.5, 22.9, 22.1, 21.6, 20.6, 19.5, 18.7, 17.9,
                           17.4, 17.3, 17.0, 17.0, 16.9, 17.0, 17.4, 17.9, 18.1, 18.1, 18.3, 18.4, 19.1, 20.1, 20.6,
                           21.4, 22.2, 23.0, 22.8, 22.0, 21.0, 19.7, 18.2, 17.2, 16.2, 15.4, 14.8, 14.4, 14.1, 13.9,
                           14.5, 15.7, 17.2, 19.1, 20.3, 21.3, 22.2, 22.8, 23.3, 23.5, 23.5, 23.3, 22.8, 22.1, 21.1,
                           20.2, 19.3, 18.5, 17.8, 17.4, 17.1, 16.9, 16.4, 16.1, 16.3, 17.8, 19.8, 21.6, 22.8, 23.6,
                           24.4, 25.1, 25.7, 26.0, 25.9, 25.5, 24.8, 23.9, 22.7, 21.6, 20.6, 19.7, 19.0, 18.5, 18.3,
                           18.1, 17.4, 17.1, 17.4, 18.5, 20.2, 21.6, 22.5, 23.2, 23.8, 24.3, 24.8, 25.0, 25.0, 24.8,
                           24.3, 23.1, 21.6, 20.3, 19.3, 18.4, 17.6, 16.8, 16.0, 15.5, 15.2, 15.0, 15.5, 17.1, 19.4,
                           21.3, 22.4, 23.2, 23.9, 24.6, 25.1, 25.4, 25.3, 25.0, 24.5, 23.6, 22.5, 21.3, 20.1, 18.8,
                           17.9, 17.6, 17.7]}}


class WeatherForecastViewTest(SimpleTestCase):
    """ Тест представления WeatherForecastView """

    def setUp(self):
        self.url = reverse('forecast:weather_forecast')
        self.response = self.client.get(self.url)

    def test_view_form(self):
        # Тест на соответствие формы экземпляру CityNameForm и наличие csrf токена
        form = self.response.context.get('form')
        self.assertIs(form, CityNameForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_view_content_test(self):
        # Тест на содержимое страницы
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertEqual(self.response.context['title'], 'Прогноз погоды')
        self.assertTemplateUsed(self.response, 'forecast/main.html')
        self.assertIn('Получить прогноз', self.response.content.decode())
        self.assertIn('X', self.response.content.decode())


class WeatherSourceViewTest(unittest.TestCase):
    """ Тест слоя ForeCastService """

    def setUp(self):
        self.forecast_repository = ForeCastRepository()
        self.forecast_service = ForeCastService()

    @patch.object(ForeCastRepository, 'get_temperature_by_geo_coord')
    @patch.object(ForeCastRepository, 'find_city')
    def test_get_weather_forecast_in_city(self, mock_find_city, mock_get_temperature_by_geo_coord):
        # Тест на получение данных погоды с правильно введённым названием города

        mock_find_city.return_value = mock_value_moscow
        mock_get_temperature_by_geo_coord.return_value = mock_value_city_temperature_data

        day_list = self.forecast_service.get_weather_forecast_in_city('Москва')
        self.assertEqual([23.7, 23.2, 23.0, 23.5, 26.0, 25.0, 25.4], self.get_temperature(day_list))

    def test_get_weather_forecast_in_city_with_invalid_data(self):
        # Тест на получение данных погоды с неправильно введённым названием города

        try:
            self.forecast_service.get_weather_forecast_in_city('--')
        except Exception as err:
            self.assertEqual(str(err), "Ошибка при запросе получения координат города")

    @staticmethod
    def get_temperature(day_list: list[Day]) -> list[str]:
        return [d.temperature for d in day_list]
