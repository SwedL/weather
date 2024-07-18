from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from .forms import CityNameForm
from datetime import date, timedelta


class WeatherForecastView(View):
    title = 'Прогноз погоды'
    form_class = CityNameForm

    def create_date(self):
        dates_week = [date.today() + timedelta(days=i) for i in range(7)]
        return dates_week

    def get(self, request):
        date_and_temperature_dict = [{'date': d, 'temperature': '-'} for d in self.create_date()]

        context = {
            'form': self.form_class,
            'title': self.title,
            'date_and_temperature_dict': date_and_temperature_dict,
        }

        return render(request, 'forecast/main.html', context=context)

    def post(self, request):

        date_and_temperature_dict = [{'date': d, 'temperature': '-'} for d in self.create_date()]

        context = {
            'form': self.form_class,
            'title': self.title,
            'date_and_temperature_dict': date_and_temperature_dict,
        }

        return render(request, 'forecast/main.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
