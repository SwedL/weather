from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from .forms import CityNameForm


class WeatherForecastView(View):
    title = 'Прогноз погоды'
    form_class = CityNameForm

    def get(self, request):

        context = {
            'form': self.form_class,
            'title': self.title,
        }

        return render(request, 'forecast/main.html', context=context)

    def post(self, request):

        context = {
            'form': self.form_class,
            # 'common_form_data': common_form_data,
            'title': 'Прогноз ГОТОВ',
        }

        return render(request, 'forecast/main.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
