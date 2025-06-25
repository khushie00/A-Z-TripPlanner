from django.db import models
from trips.models import Trip

class Accommodation(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='accommodations')
    hotel_name = models.CharField(max_length=150)
    address = models.TextField()
    check_in = models.DateField()
    check_out = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.hotel_name} for {self.trip.title}"
