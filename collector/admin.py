from django.contrib import admin

from . import models


class CityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'country_code', 'latitude', 'longitude',)
    search_fields = ('pk', 'name', 'country_code', 'latitude', 'longitude',)
    empty_value_display = '-empty-'


class ReadingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'city', 'main', 'date_created',)
    search_fields = ('pk', 'city__name', 'date_created', )
    empty_value_display = '-empty-'


admin.site.register(models.City, CityAdmin)
admin.site.register(models.Reading, ReadingAdmin)
