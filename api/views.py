import datetime
from django.utils import timezone
from rest_framework import generics
from django.db.models import Count
from .models import NavigationRecord, Vehicle
from .serializers import NavigationRecordSerializer, VehicleSerializer
from .utils import create_random_plate


def latest_records():
    """
    The function that returns the list of last points per vehicle
    that have sent navigation data in the last  48 hours.

    It basically calculates 48 hours time range to use it in the query.
    Then, filter the data with respect to calculated last2days variable.
    At the end, sort the data and pick the lates records per vehicle.
    """
    # Get current time
    now = timezone.now()
    # Calculate the exact time range
    last2days = now - datetime.timedelta(seconds=2*86400)
    # Query set 
    query_set = NavigationRecord.objects.filter(datetime__range = [last2days, now]).order_by('vehicle', '-datetime').distinct('vehicle')
    # Return to view
    return query_set

class recent_records_view(generics.ListAPIView):
    # Get the queryset by calling latest_records function
    queryset = latest_records()
    serializer_class = NavigationRecordSerializer


class vehicles_view(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

