from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Room, Reservation
from django.utils import timezone
from datetime import timedelta

class RoomBookingTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.room = Room.objects.create(room_number='101', capacity=2, description='Test Room')
        self.reservation = Reservation.objects.create(room=self.room, user=self.user, check_in_date=timezone.now().date(), check_out_date=timezone.now().date() + timedelta(days=1))

    def test_room_availability_api(self):
        response = self.client.get('/api/rooms/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('available', response.data)
        self.assertIn('reserved', response.data)
        self.assertIn('date', response.data)

    def test_room_booking_api_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {'room_name': '101', 'start': str(timezone.now().date()), 'end': str(timezone.now().date() + timedelta(days=1))}
        response = self.client.post('/api/book/room/', data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.data)
        self.assertIn('room', response.data)
        self.assertIn('room_name', response.data)
        self.assertIn('start', response.data)
        self.assertIn('end', response.data)

    def test_room_booking_api_unauthenticated(self):
        data = {'room_name': '101', 'start': str(timezone.now().date()), 'end': str(timezone.now().date() + timedelta(days=1))}
        response = self.client.post('/api/book/room/', data)
        self.assertEqual(response.status_code, 401)
        # Проверьте, что в ответе есть ключ 'error'
        self.assertIn('error', response.data)

    def test_room_detail_view(self):
        response = self.client.get('/api/room/101/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('room_number', response.data)
        self.assertIn('capacity', response.data)
        self.assertIn('description', response.data)

    def test_user_registration_view(self):
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('username', response.data)
        self.assertIn('id', response.data)
