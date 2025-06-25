from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country', 'city', 'state']

class DestinationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
