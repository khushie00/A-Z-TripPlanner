from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Trip
from .serializers import TripSerializer
from rest_framework.permissions import IsAuthenticated

class TripListCreateView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TripRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]


from .models import Itinerary
from .serializers import ItinerarySerializer

class ItineraryListCreateView(generics.ListCreateAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

class ItineraryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]
