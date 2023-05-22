import os
import requests

from collector import models
from requests.exceptions import ConnectionError


API_KEY = os.getenv('API_KEY')
URL = 'https://api.openweathermap.org/data/2.5/weather?'


def clean_data(response: dict, city: int):
    main = response.pop('main', None)
    _ = models.Reading.objects.create(
        city_id=city,
        main=main,
        others=response
    )


def get_weather_from_api():
    cities = models.City.objects.all()
    for city in cities:
        lat = city.latitude
        lon = city.longitude
        url = URL + f'lat={lat}&lon={lon}&appid={API_KEY}'
        try:
            response = requests.get(
                url=url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
        except ConnectionError:
            return 'Отсутствует подключение к интернету'
        match response.status_code:
            case 200:
                clean_data(response.json(), city.id)
            case 401:
                return 'Неверный API ключ'
            case _:
                return 'Api недоступно'
