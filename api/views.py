from rest_framework import generics
from django.db.models import F, Func, Value, CharField
from .models import NavigationRecord, Vehicle
from .serializers import NavigationRecordSerializer, VehicleSerializer
from .utils import create_random_plate

import datetime
import random
from django.utils import timezone


"""
The function that returns the list of last points per vehicle
that have sent navigation data in the last  48 hours. 
"""

def latest_records():
    now = timezone.now()
    # vehicle = Vehicle.objects.filter(id=15).first()
    # for i in range(20):
    #     past = now - datetime.timedelta(seconds=random.randint(0, 10*86400))
    #     record = NavigationRecord.objects.create(vehicle=vehicle, latitude=round(random.uniform(1,50), 2), longitude=round(random.uniform(1,50), 2), datetime=past)
    #     record.save()
    last2days = now - datetime.timedelta(seconds=2*86400)
    # print("---------------------------")
    # print(NavigationRecord.objects.annotate(plate="vehicle"))
    # print("---------------------------")
    query_set = NavigationRecord.objects.filter(datetime__range = [last2days, now])
    query_set_formatted = query_set.annotate(formatted_date=Func(F('datetime'), Value('DD-MM-YYYY HH:MM:SS'), function='to_char', output_field=CharField()))
    return query_set_formatted

class recent_records_view(generics.ListCreateAPIView):
    # Get the queryset by calling latest_records function
    queryset = latest_records()
    serializer_class = NavigationRecordSerializer


class vehicles_view(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()#.filter(plate__startswith="23")
    serializer_class = VehicleSerializer

