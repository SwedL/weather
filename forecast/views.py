from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views import View
from django.core.cache import cache
from .forms import CityNameForm
from datetime import date, timedelta
from common.views import WeatherSource
from django.urls import reverse
from django.views.decorators.http import require_http_methods


class WeatherForecastView(WeatherSource, View):
    title = 'Прогноз погоды'
    form_class = CityNameForm

    @property
    def create_date(self):
        dates_week = [date.today() + timedelta(days=i) for i in range(7)]
        return dates_week

    def get(self, request):
        date_and_temperature_list = [{'date': d, 'temperature': '-'} for d in self.create_date]

        context = {
            'form': self.form_class,
            'title': self.title,
            'date_and_temperature_list': date_and_temperature_list,
        }

        return render(request, 'forecast/main.html', context=context)

    def post(self, request):
        error = None

        city = request.POST['city']
        temperatures_by_week = cache.get(city)

        # кэшируем данные температуры по городу на 1 час
        if not temperatures_by_week:
            temperatures_by_week, error = self.get_weather_forecast(city)
            cache.set(city, temperatures_by_week, 3600)

        date_and_temperature_list = [{'date': d, 'temperature': t} for d, t in
                                     zip(self.create_date, temperatures_by_week)]

        context = {
            'form': self.form_class(request.POST),
            'title': self.title,
            'date_and_temperature_list': date_and_temperature_list,
            'error': error,
        }

        return render(request, 'forecast/main.html', context=context)


def clear_search(request):
    """ Функция для очистки полей формы поиска CityNameForm """

    redirect_url = reverse('forecast:weather_forecast')
    return HttpResponseRedirect(redirect_url)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
