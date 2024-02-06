from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=100)
    total_time = models.DurationField()
    date_create = models.DateField()
    date_finish = models.DateField()

    def __str__(self):
        return self.name
