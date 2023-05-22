# Generated by Django 4.2.1 on 2023-05-20 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('country_code', models.CharField(max_length=2, verbose_name='Код страны')),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.JSONField(verbose_name='Основное')),
                ('others', models.JSONField(verbose_name='Остальное')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Показания',
                'verbose_name_plural': 'Показания',
            },
        ),
    ]
