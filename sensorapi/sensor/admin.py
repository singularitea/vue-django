from django.contrib import admin
from sensor.models import SensorDetail, SensorReading

admin.site.register(SensorDetail)

admin.site.register(SensorReading)
