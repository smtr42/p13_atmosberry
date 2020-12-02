from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Reading, Sensor
from .serializers import ReadingSerializer, SensorSerializer


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


class SensorView(generics.ListCreateAPIView):
    serializer_class = SensorSerializer

    def get_queryset(self):
        get_sensor = Sensor.objects.all()
        return get_sensor

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
    
    def create(self, validated_data):
        tracks_data = validated_data.pop('data')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album