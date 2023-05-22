from django.contrib import admin
from django.urls import path

from api.views import WeatherAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WeatherAPIView.as_view())
]
