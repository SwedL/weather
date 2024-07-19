"""Схемы URL для forecast"""

from django.urls import path

from .views import WeatherForecastView, clear_search

app_name = 'forecast'

urlpatterns = [
    path('', WeatherForecastView.as_view(), name='weather_forecast'),
    path('clear-search/', clear_search, name='clear_search'),
]
