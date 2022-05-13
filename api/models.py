from django.db import models

# Create your models here.

class NavigationRecord(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def format_date(self):
        return self.datetime.strftime("%d.%m.%Y %H:%M:%S")

class Vehicle(models.Model):
    plate = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.plate

