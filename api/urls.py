from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('homepage.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('weather-forecast/', include('weather.urls',), name='forecast')
]
