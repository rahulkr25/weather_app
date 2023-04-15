from django.db import models
from django.core.cache import cache


class Weather(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    weather_description = models.CharField(max_length=255)

    def __str__(self):
        return self.city
