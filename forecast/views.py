from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View


class WeatherForecastView(View):
    title = 'Прогноз погоды по выбранному городу'

    def get(self, request):

        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'common_form_data': common_form_data,
            'title': self.title,
            'staff': request.user.has_perm('forecast.change_employee'),
        }

        return render(request, 'forecast/department.html', context=context)

    def post(self, request):

        form = SearchEmployeeForm(request.POST)

        # обновление словаря common_form_data
        if form.is_valid():
            common_form_data.update(form.cleaned_data)


        context = {
            'employees': page_obj,
            'form': form,
            'paginator_range': page_obj.paginator.get_elided_page_range(page_obj.number),
            'common_form_data': common_form_data,
            'title': self.title,
            'staff': request.user.has_perm('forecast.change_employee'),
        }

        return render(request, 'forecast/department.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
