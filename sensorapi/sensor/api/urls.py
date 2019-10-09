from django.urls import path
from sensor.api.views import sensor_detail_list_create_api_view

urlpatterns = [
    path("sensors/", sensor_detail_list_create_api_view, name="sensor-list")
]