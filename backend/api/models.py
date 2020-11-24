from django.db import models
from django.conf import settings


class Device(models.Model):
    """ """

    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="device",
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name


class Address(models.Model):
    """ """

    line1 = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    # RELATION
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="address",
        on_delete=models.CASCADE,
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)


class Reading(models.Model):
    data = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()


class Sensor(models.Model):
    """ """

    TEMPERATURE = "T"
    HUMIDITY = "Hu"
    PRESSURE = "P"
    SENSOR_TYPE_CHOICE = [
        (TEMPERATURE, "Temperature"),
        (HUMIDITY, "Humidity"),
        (PRESSURE, "Pressure"),
    ]
    sensor_type = models.CharField(
        max_length=2,
        choices=SENSOR_TYPE_CHOICE,
        default=TEMPERATURE,
    )
    name = models.CharField(max_length=150)

    # RELATION
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    reading = models.OneToOneField(
        Reading,
        on_delete=models.CASCADE,
    )
