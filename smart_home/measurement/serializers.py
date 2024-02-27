from rest_framework import serializers
from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor_id']


class CreateMeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor_id']

    def create(self, validated_data):

        measurement = Measurement.objects.create(
            sensor_id=self.initial_data.get('sensor_id'),
            temperature=self.initial_data.get('temperature'),
            created_at=self.initial_data.get('created_at'),
        )
        # measurement = Measurement.objects.create(
        #     sensor_id=self.initial_data.get('sensor_id'),
        #     temperature=validated_data.get('temperature'),
        #     created_at=validated_data.get('created_at'),
        # )
        return measurement


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
