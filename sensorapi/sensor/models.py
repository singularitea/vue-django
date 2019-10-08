from django.db import models
from taggit.managers import TaggableManager

# Sensor types for grouping and mass changes
class SensorType(models.Model):
    type_name = models.CharField(max_length=70)

# 
class SensorDetails(models.Model):
    sensor_name = models.CharField(max_length=70)
    latitude = models.DecimalField(max_digits=14, decimal_places=4)
    longitude = models.DecimalField(max_digits=14, decimal_places=4)
    easting = models.DecimalField(max_digits=14, decimal_places=4)
    northing = models.DecimalField(max_digits=14, decimal_places=4)
    elevation = models.DecimalField(max_digits=10, decimal_places=4)
    tags = TaggableManager()
    def __str__(self):
        return str(self.sensor_name)

class SensorReading(models.Model):
    sensor_name = models.ForeignKey(SensorDetails, db_column='sensor_name', on_delete=models.CASCADE)
    reading_date = models.DateTimeField()
    reading = models.DecimalField(max_digits=14, decimal_places=4)
    def __str__(self):
        return "{} - {} - {}".format(self.instrument_id,self.read_date,self.reading)
        #return str(self.instrument_id)