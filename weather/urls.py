from django.urls import path
from .views import ForecastWeatherView


urlpatterns = [
    path('', (ForecastWeatherView.as_view())),
]
