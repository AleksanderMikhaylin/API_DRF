from django.db import models
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return 'Описание датчика'


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensors')

    def __str__(self):
        return 'Показания'
