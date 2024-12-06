from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import *


# Create your views here.

def index(request):
    return render(request, 'reservation/index.html')


@login_required()
def reservation(request):
    reserve = DoctorTime.objects.all()
    name_dr = DrUser.objects.all()
    context = {
        'reserve': reserve,
        'name_dr': name_dr,
    }
    return render(request, 'reservation/reserve_page.html', context)


@login_required()
def verifi_reservation(request, pk):
    user = request.user
    reserve = DoctorTime.objects.get(pk=pk)
    if request.method == 'POST':
        reserve.is_booked = True
        reserve.sick_name = user.get_full_name()
        reserve.save()
        return redirect('profile_user', )
    context = {
        'reserve': reserve,
    }
    return render(request, 'reservation/verifi_reserve.html', context)


@login_required()
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            DoctorTime.objects.create(user=user.dr_user, day_of_week=cd['day_of_week'], date=cd['date'],
                                      hour=cd['hour'])

            return redirect('profile_dr')

    else:
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservation/create_time_dr.html', context)
