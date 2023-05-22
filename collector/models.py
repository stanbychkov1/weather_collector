from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    country_code = models.CharField(max_length=2, verbose_name='Код страны')
    latitude = models.DecimalField(max_digits=6, decimal_places=4,
                                   verbose_name='Широта')
    longitude = models.DecimalField(max_digits=6, decimal_places=4,
                                    verbose_name='Долгота')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Reading(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.SET_NULL,
                             verbose_name='Город', null=True)
    main = models.JSONField(verbose_name='Основное')
    others = models.JSONField(verbose_name='Остальное')
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата и время создания')

    def __str__(self):
        return f'Погода в городе {self.city.name} - {self.main["temp"]}'

    class Meta:
        verbose_name = 'Показания'
        verbose_name_plural = 'Показания'
        ordering = ('-date_created',)
