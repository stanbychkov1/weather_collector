from rest_framework import generics

from api import serializers
from collector import models


class WeatherAPIView(generics.ListAPIView):
    serializer_class = serializers.ReadingSerializer

    def get_queryset(self):
        qty = models.City.objects.count()
        queryset = models.Reading.objects.select_related('city')[:qty]
        return queryset
