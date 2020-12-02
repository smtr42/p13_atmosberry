from rest_framework import serializers

from .models import Address, Device, Reading, Sensor


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = (
            "data",
            "timestamp",
            "sensor",
        )
        depth = 2

class SensorSerializer(serializers.ModelSerializer):
    reading = ReadingSerializer(many=True)
    class Meta:
        model = Sensor
        fields = (
            "sensor_type",
            "name",
            "sensor_reading",
        )

    def create(self, validated_data):
        readings_data = validated_data.pop('data')
        sensor = Sensor.objects.create(**validated_data)
        for readings in readings_data:
            Reading.objects.create(sensor=sensor, **readings)
        return sensor



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "city",
            "country",
        )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("name",)
