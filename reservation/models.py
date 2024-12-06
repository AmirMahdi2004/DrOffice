from django.db import models
from account.models import *


# Create your models here.
class DoctorTime(models.Model):
    user = models.ForeignKey(DrUser, on_delete=models.CASCADE, related_name='doctor_time')
    DAY_CHOICES = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]
    day_of_week = models.IntegerField(choices=DAY_CHOICES, default=1)
    hour = models.TimeField()
    date = models.DateField()
    is_booked = models.BooleanField(default=False)
    sick_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user}"
