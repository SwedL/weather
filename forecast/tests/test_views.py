from http import HTTPStatus

from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class WeatherForecastViewTest(SimpleTestCase):
    """ Тест представления WeatherForecastView """

    def setUp(self):
        self.url = reverse('forecast:weather_forecast')
        self.response = self.client.get(self.url)

    def test_view_form(self):
        # Тест на соответствие формы экземпляру CityNameForm и наличие csrf токена
        form = self.response.context.get('form')
        # self.assertIsInstance(form, CityNameForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_view_content_test(self):
        # Тест на содержимое страницы
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertEqual(self.response.context['title'], 'Прогноз погоды')
        self.assertTemplateUsed(self.response, 'forecast/main.html')
        self.assertIn('Получить прогноз', self.response.content.decode())
        self.assertIn('X', self.response.content.decode())
