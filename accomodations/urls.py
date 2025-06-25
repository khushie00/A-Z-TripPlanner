from django.urls import path
from .views import AccommodationListCreateView, AccommodationRetrieveUpdateDeleteView

urlpatterns = [
    path('', AccommodationListCreateView.as_view(), name='accommodation-list-create'),
    path('<int:pk>/', AccommodationRetrieveUpdateDeleteView.as_view(), name='accommodation-detail'),
]
