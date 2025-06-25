from django.urls import path
from .views import TripListCreateView, TripRetrieveUpdateDeleteView
from .views import ItineraryListCreateView, ItineraryRetrieveUpdateDeleteView

urlpatterns = [
    path('', TripListCreateView.as_view(), name='trip-list-create'),
    path('<int:pk>/', TripRetrieveUpdateDeleteView.as_view(), name='trip-detail'),
    
    path('itineraries/', ItineraryListCreateView.as_view(), name='itinerary-list-create'),
    path('itineraries/<int:pk>/', ItineraryRetrieveUpdateDeleteView.as_view(), name='itinerary-detail'),
]
