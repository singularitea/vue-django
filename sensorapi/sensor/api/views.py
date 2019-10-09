from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sensor.models import SensorDetail
from sensor.api.serializers import SensorDetailSerializer

@api_view(["GET", "POST"])
def sensor_detail_list_create_api_view(request):

    if request.method == "GET":
        sensors = SensorDetail.objects.filter()
        serializer = SensorDetailSerializer(sensors, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)