from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from destinations.models import Destination

User = get_user_model()

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.destination.name}"


class Itinerary(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='itineraries')
    day = models.PositiveIntegerField()
    date = models.DateField()
    activities = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Day {self.day} - {self.trip.title}"
