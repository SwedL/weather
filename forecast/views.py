from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from forecast.services.forecast import ForeCastService

from .forms import CityNameForm


class WeatherForecastView(View):
    """ Представление главной страницы прогноза погоды """

    title = 'Прогноз погоды'
    form_class = CityNameForm
    forecast_service = ForeCastService()

    def get(self, request) -> HttpResponse:
        date_and_temperature_list = [{'date': day, 'temperature': '-'} for day in self.forecast_service.weekday]

        context = {
            'form': self.form_class,
            'title': self.title,
            'date_and_temperature_list': date_and_temperature_list,
        }

        return render(request=request, template_name='forecast/main.html', context=context)

    def post(self, request) -> HttpResponse:
        context = {
            'form': self.form_class(request.POST),
            'title': self.title,
        }

        try:
            date_and_temperature_list = self.forecast_service.get_weather_forecast_in_city(
                city_name=request.POST['city']
            )
            context['date_and_temperature_list'] = date_and_temperature_list
        except Exception as err:
            context['date_and_temperature_list'] = self.forecast_service.create_date_and_temperature_list()
            context['error'] = str(err)

        return render(request=request, template_name='forecast/main.html', context=context)


def clear_search(request) -> HttpResponseRedirect:
    """ Функция для очистки полей формы поиска CityNameForm """

    redirect_url = reverse('forecast:weather_forecast')
    return HttpResponseRedirect(redirect_url)


def pageNotFound(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
