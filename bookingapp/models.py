from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.room_number

    def is_available(self, check_in_date, check_out_date):
        reservations = self.reservation_set.filter(
            Q(check_in_date__lte=check_in_date, check_out_date__gte=check_in_date) |
            Q(check_in_date__lte=check_out_date, check_out_date__gte=check_out_date) |
            Q(check_in_date__gte=check_in_date, check_out_date__lte=check_out_date)
        )
        return not reservations.exists()

    @property
    def is_available_now(self):
        today = timezone.now().date()
        return self.is_available(today, today)


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.room} ({self.check_in_date} to {self.check_out_date})"


