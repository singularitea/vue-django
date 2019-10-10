from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

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

@api_view(["GET", "PUT", "DELETE"])
def sensor_detail_api_view(request, pk):
    try:
        sensor = SensorDetail.objects.get(pk=pk)
    except SensorDetail.DoesNotExist:
            return Response({"error": {
                                "code": 404,
                                "message": "Sensor not found",
                            }}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET":
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)
    
    if request.method =="PUT":
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SensorDetailListCreateAPIView(APIView):

    def get(self, request):
        sensors = SensorDetail.objects.filter()
        serializer = SensorDetailSerializer(sensors, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorDetailAPIView(APIView):

    def get_object(self, pk):
        sensor = get_object_or_404(SensorDetail, pk=pk)
        return sensor

    def get(self, request, pk):
        sensor = self.get_object(pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

    def put(self, request, pk):
        sensor = self.get_object(pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sensor = self.get_object(pk)
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)