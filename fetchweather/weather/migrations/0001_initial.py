# Generated by Django 4.2 on 2023-04-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('weather_description', models.CharField(max_length=255)),
            ],
        ),
    ]
