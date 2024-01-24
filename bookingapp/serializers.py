from rest_framework import serializers
from .models import Room, Reservation
from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'capacity', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class RoomBookingSerializer(serializers.Serializer):
    room_name = serializers.CharField(max_length=50)
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def create(self, validated_data):
        room_name = validated_data['room_name']
        start = validated_data['check_in_date']
        end = validated_data['check_in_date']
        room = Room.objects.get(room_number=room_name)

        reservation = Reservation.objects.create(
            room=room,
            user=self.context['request'].user,
            check_in_date=start,
            check_out_date=end
        )
        return reservation

from django.utils import timezone
class RoomDetailSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['room_number','capacity', 'description', 'is_available']

    def get_is_available(self, obj):
        today = timezone.now().date()
        return obj.is_available(today, today)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)