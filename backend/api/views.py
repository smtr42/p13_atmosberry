from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Reading, Sensor
from .serializers import ReadingSerializer


class ReadingView(generics.ListCreateAPIView):
    serializer_class = ReadingSerializer

    def get_queryset(self):
        get_reading = Reading.objects.all()
        return get_reading

    def create(self, request, *args, **kwargs):
        reading_data = request.data

        new_reading = Reading.objects.create(
            sensor=Sensor.objects.get(name=reading_data["sensor"]),
            data=reading_data["data"],
            timestamp=reading_data["timestamp"],
        )
        new_reading.save()
        serializer = ReadingSerializer(new_reading)
        return Response(serializer.data)
