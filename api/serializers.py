from rest_framework import serializers
from collector import models


class ReadingSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = models.Reading
        fields = ('city', 'main',)
