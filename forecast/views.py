from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from .forms import CityNameForm
from datetime import date, timedelta
from common.views import WeatherSource


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
        city = request.POST['city']

        date_and_temperature_list = [{'date': d, 'temperature': t} for d, t in
                                     zip(self.create_date, self.get_weather_forecast(city))]

        context = {
            'form': self.form_class,
            'title': self.title,
            'date_and_temperature_list': date_and_temperature_list,
        }

        return render(request, 'forecast/main.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
