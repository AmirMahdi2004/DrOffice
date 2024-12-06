from django import forms
from .models import *


class ReservationForm(forms.ModelForm):
    class Meta:
        model = DoctorTime
        fields = ['day_of_week', 'date', 'hour']
