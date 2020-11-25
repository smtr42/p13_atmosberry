from django.contrib import admin

from .models import Address, Device, Reading, Sensor

admin.site.register([Reading, Sensor, Address, Device])
