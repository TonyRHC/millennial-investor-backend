# Generated by Django 3.0.5 on 2020-04-28 04:21

from django.db import migrations

def create_data(apps, schema_editor):
    Stock = apps.get_model('stocks', 'Stock')
    Stock(ticker="AAPL").save()


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
    ]
