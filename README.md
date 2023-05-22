# Weather Collector

Собирает данные погоды из городов.


Требования:
1. Docker ([установить](https://docs.docker.com/engine/install/))
2. Docker-compose ([установить](https://docs.docker.com/compose/install/))

Launch app:
Сперва скачайте приложение:
```bash
git clone git@github.com:stanbychkov1/weather_collector.git
````
Создайте файл .env о следующими данными <ваши данные>:
````
API_KEY = '<API KEY openweather>'

DJANGO_DEBUG = False
SECRET_KEY = '<Django secret key>>'

REDIS_HOST = 'redis'

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DJANGO_DATABASE_HOST=db
DJANGO_DATABASE_PORT=5432
````
Запустите команду:
```bash
docker-compose up
````
По адресу <domain_name>:8000 будут доступны последние данные по погоде из городов.