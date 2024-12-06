from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(DoctorTime)
class DoctorTime(admin.ModelAdmin):
    list_display = ('user', 'hour', 'day_of_week', 'is_booked')


