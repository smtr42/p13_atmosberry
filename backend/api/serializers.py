from rest_framework import serializers

from .models import Address, Device, Reading, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = (
            "sensor_type",
            "name",
        )


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = (
            "data",
            "timestamp",
            "sensor",
        )
        depth = 2


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
