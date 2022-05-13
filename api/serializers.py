from rest_framework import serializers
from .models import NavigationRecord, Vehicle

class NavigationRecordSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate')

    class Meta:
        model = NavigationRecord
        fields = ('latitude', 'longitude', 'vehicle_plate', 'datetime')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'plate')

