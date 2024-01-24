# Ваш файл urls.py

from django.urls import path
from .views import RoomAvailabilityAPI, RoomBookingAPIView, RoomDetailView

urlpatterns = [
    path('api/rooms/', RoomAvailabilityAPI.as_view(), name='room_availability_api'),
    path('api/book/room/', RoomBookingAPIView.as_view(), name='room_booking_api'),
    path('api/room/<str:room_number>/', RoomDetailView.as_view(), name='room_booking_with_name')
]
