# Generated by Django 3.0.5 on 2020-04-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Future',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('creationDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
