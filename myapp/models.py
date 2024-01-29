from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # В реальном проекте лучше использовать хэширование паролей

    def __str__(self):
        return self.username

class Route(models.Model):
    name = models.CharField(max_length=100)
    # Другие поля, связанные с маршрутом

    def __str__(self):
        return self.name

class GasStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # Другие поля, связанные с АЗС

    def __str__(self):
        return self.name

class Refueling(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    # Другие поля, связанные с заправками на маршруте

    def __str__(self):
        return f"{self.route.name} - {self.gas_station.name}"
