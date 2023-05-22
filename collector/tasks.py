from weather_collector.celery_app import app

from .services import get_weather_from_api


@app.task(name='weather_collector')
def weather_collector():
    result = get_weather_from_api()
    if result:
        return result
    return 'Success'
