from django.urls import path
# from sensor.api.views import (sensor_detail_api_view,
#                             sensor_detail_list_create_api_view)
from sensor.api.views import (SensorDetailListCreateAPIView,
                            SensorDetailAPIView)


urlpatterns = [
    # path("sensors/", sensor_detail_list_create_api_view, name="sensor-list"),
    # path("sensors/<int:pk>", sensor_detail_api_view, name="sensor-details")

    path("sensors/", SensorDetailListCreateAPIView.as_view(), name="sensor-list"),
    path("sensors/<int:pk>", SensorDetailAPIView.as_view(), name="sensor-details")
]