from django.shortcuts import render
from rest_framework import generics, status
# Create your views here.
from rest_framework.views import APIView

from .models import Room, Reservation
from .serializers import RoomSerializer, RoomBookingSerializer, RoomDetailSerializer, LoginSerializer
from django.shortcuts import get_object_or_404



from rest_framework import generics
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer
from django.utils import timezone



class RoomAvailabilityAPI(generics.ListAPIView):
    serializer_class = RoomSerializer
    # permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        rooms = Room.objects.all()
        available_rooms = [room for room in rooms if room.is_available_now]
        reserved_rooms = [room for room in rooms if not room.is_available_now]
        serializer_available = self.get_serializer(available_rooms, many=True)
        serializer_reserved = self.get_serializer(reserved_rooms, many=True)

        return Response({
            'available': serializer_available.data,
            'reserved': serializer_reserved.data,
            'date': today
        })

class RoomBookingAPIView(APIView):
    # permission_classes = [IsAuthenticated,]
    def post(self, request, *args, **kwargs):
        serializer = RoomBookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            room_name = serializer.validated_data['room_name']
            start = serializer.validated_data['start']
            end = serializer.validated_data['end']

            room = get_object_or_404(Room, room_number=room_name)
            aviable_from = get_object_or_404(Reservation, room=room.id)
            # Check if the room is available for the specified period
            if room.is_available(start, end):
                if request.user.is_authenticated:
                    # Create a new reservation
                    reservation = Reservation.objects.create(
                        room=room,
                        user=request.user, # Assuming the Client is associated with the User
                        check_in_date=start,
                        check_out_date=end
                    )

                    return Response({
                        'message': 'Booking successful for you',
                        'room': room.capacity,
                        'room_name': room.room_number,
                        'start': start,
                        'end': end
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({
                    'error': 'Room not available for the specified period',
                    'available_from': aviable_from.check_out_date
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated,]
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    lookup_field = 'room_number'

from .serializers import UserSerializer
from django.contrib.auth.models import User
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
