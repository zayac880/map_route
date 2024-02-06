from django.db import models

from routes.models import Route


class GasStation(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)  # Регион
    issuer_number = models.CharField(max_length=20)  # Номер эмитента
    station_number = models.CharField(max_length=20)  # Номер АЗС
    address = models.TextField()  # Адрес
    related_services = models.TextField()  # Объекты сопутствующего сервиса
    additional_services = models.TextField()  # Дополнительные услуги
    ai_92 = models.BooleanField()  # АИ-92
    ai_95 = models.BooleanField()  # АИ-95
    dt = models.BooleanField()  # ДТ
    dt_arctic = models.BooleanField()  # ДТ Арктика
    ai_92_taneko = models.BooleanField()  # АИ-92 Танеко
    ai_98_taneko = models.BooleanField()  # АИ-98 Танеко
    dt_taneko = models.BooleanField()  # ДТ ТАНЕКО
    sug = models.BooleanField()  # СУГ
    electric_charging = models.BooleanField()  # Электрозарядка
    ai_98 = models.BooleanField()  # АИ-98
    ai_95_taneko = models.BooleanField()  # АИ-95 Танеко
    adblue = models.BooleanField()  # AdBlue
    ai_100 = models.BooleanField()  # АИ-100
    ai_80 = models.BooleanField()  # АИ-80
    dt_winter = models.BooleanField()  # ДТ (зимнее)
    kpg = models.BooleanField()  # КПГ

    def __str__(self):
        return self.name


class Refueling(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=50)  # Тип топлива (например, АИ-95, ДТ)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Количество топлива
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость заправки
    date = models.DateField()  # Дата заправки

    def __str__(self):
        return f"{self.route.name} - {self.gas_station.name} - {self.date}"

