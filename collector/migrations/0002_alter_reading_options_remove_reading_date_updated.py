# Generated by Django 4.2.1 on 2023-05-20 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reading',
            options={'ordering': ('-date_created',), 'verbose_name': 'Показания', 'verbose_name_plural': 'Показания'},
        ),
        migrations.RemoveField(
            model_name='reading',
            name='date_updated',
        ),
    ]
