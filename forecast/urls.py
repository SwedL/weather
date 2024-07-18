"""Схемы URL для forecast"""

from django.urls import path

from .views import WeatherForecastView

app_name = 'forecast'

urlpatterns = [
    path('', WeatherForecastView.as_view(), name='weather_forecast'),
]
