from django.db import models
from taggit.managers import TaggableManager

class SensorDetail(models.Model):
    sensor_name = models.CharField(unique=True, max_length=70)
    latitude = models.DecimalField(max_digits=14, decimal_places=4)
    longitude = models.DecimalField(max_digits=14, decimal_places=4)
    easting = models.DecimalField(max_digits=14, decimal_places=4)
    northing = models.DecimalField(max_digits=14, decimal_places=4)
    elevation = models.DecimalField(max_digits=10, decimal_places=4)
    install_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    def __str__(self):
        return str(self.sensor_name)
    class Meta:
        ordering = ['sensor_name']


class SensorReading(models.Model):
    sensor_name = models.ForeignKey(SensorDetail, db_column='sensor_name', on_delete=models.CASCADE)
    reading_date = models.DateTimeField()
    reading = models.DecimalField(max_digits=14, decimal_places=4)
    def __str__(self):
        return "{} - {} - {}".format(self.sensor_name,self.reading_date,self.reading)
        #return str(self.instrument_id)