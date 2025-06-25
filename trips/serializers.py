from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Trip
        fields = '__all__'

from .models import Itinerary

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    itineraries = ItinerarySerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'
