from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from sensor.models import SensorDetail

class SensorDetailSerializer(serializers.ModelSerializer):

    time_since_install =serializers.SerializerMethodField()

    class Meta:
        model = SensorDetail
        # fields = "_all_" # all fields
        # fields = ("sensor_name", "easting" , "northing") # only these fields
        exclude = ("id",)

    def get_time_since_install(self, object):
        install_date = object.install_date
        now = datetime.now()
        time_delta = timesince(install_date, now)
        return time_delta

    def validate(self, data):
        # check that easting and northing are not the same
        if data["easting"] == data["northing"]:
            raise serializers.ValidationError("Easting and Northing cannot be same value")
        return data
    
    def validate_sensor_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("sensor name must be at least 3 characters")
        return value

# class SensorDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     sensor_name = serializers.CharField()
#     latitude = serializers.DecimalField(max_digits=20, decimal_places=5, coerce_to_string=None, max_value=None, min_value=None)
#     longitude = serializers.DecimalField(max_digits=20, decimal_places=5, coerce_to_string=None, max_value=None, min_value=None)
#     easting = serializers.DecimalField(max_digits=20, decimal_places=5, coerce_to_string=None, max_value=None, min_value=None)
#     northing = serializers.DecimalField(max_digits=20, decimal_places=5, coerce_to_string=None, max_value=None, min_value=None)
#     elevation = serializers.DecimalField(max_digits=20, decimal_places=5, coerce_to_string=None, max_value=None, min_value=None)
#     install_date = serializers.DateField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return SensorDetail.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.sensor_name = validated_data.get('sensor_name', instance.sensor_name)
#         instance.latitude = validated_data.get('latitude', instance.latitude)
#         instance.longitude = validated_data.get('longitude', instance.longitude)
#         instance.easting = validated_data.get('easting', instance.easting)
#         instance.northing = validated_data.get('northing', instance.northing)
#         instance.elevation = validated_data.get('elevation', instance.elevation)
#         instance.install_date = validated_data.get('install_date', instance.install_date)
#         instance.save()
#         return instance

