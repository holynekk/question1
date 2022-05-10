from rest_framework import serializers
from .models import NavigationRecord, Vehicle

class NavigationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationRecord
        fields = ('id', 'vehicle', 'datetime', 'latitude', 'longitude')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'plate')

