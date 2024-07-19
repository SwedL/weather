from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.urls.base import resolve

from forecast.views import WeatherForecastView


class ForecastURLsTest(TestCase):
    """ Тест URLs forecast"""

    def test_root_url_resolves_to_homepage_view(self):
        # проверка соответствия представления для данного URL
        found = resolve(reverse('forecast:weather_forecast'))
        self.assertEqual(found.func.view_class, WeatherForecastView)

    def test_homepage_url(self):
        # проверка успешного запроса клиента
        response = self.client.get(reverse('forecast:weather_forecast'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
