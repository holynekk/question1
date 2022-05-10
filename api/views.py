from rest_framework import generics
from .models import NavigationRecord, Vehicle
from .serializers import NavigationRecordSerializer, VehicleSerializer
from .utils import create_random_plate

"""
The function that returns the list of last points per vehicle
that have sent navigation data in the last 48 hours. 
"""

def latest_records():
    return NavigationRecord.objects.all()

class recent_records_view(generics.ListCreateAPIView):
    # Get the queryset by calling latest_records function
    queryset = latest_records()
    serializer_class = NavigationRecordSerializer


class vehicles_view(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()#.filter(plate__startswith="23")
    serializer_class = VehicleSerializer

