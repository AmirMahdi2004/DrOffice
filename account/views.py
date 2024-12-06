from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reservation.models import DoctorTime
from .models import *
from .forms import *


# Create your views here.
def register_dr(request):
    if request.method == 'POST':
        form = DrRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'ثبت نام با موفقیت انجام شد ')
            return redirect('login')
    else:
        form = DrRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register_dr.html', context)


def register_user(request):
    if request.method == 'POST':
        form = SickRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SickRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register_user.html', context)


def login_view(request):
    if request.method == 'POST':
        national_code = request.POST['national_code']
        password = request.POST['password']
        user = authenticate(request, national_code=national_code, password=password)
        if user is not None:
            login(request, user=user)
            if user.user_type == 1:
                return redirect('profile_dr')
            else:
                return redirect('profile_user')
        else:
            return HttpResponse('Invalid crendntials')

    return render(request, 'account/login.html')


@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required()
def profile_user(request):
    user = User.objects.get(id=request.user.id)
    user_sick = SickUser.objects.get(user=user)
    time_dr = DoctorTime.objects.all().filter(sick_name=user)

    context = {
        "user": user,
        "user_sick": user_sick,
        "time_dr": time_dr,
    }
    return render(request, 'account/profile_user.html', context)


@login_required()
def profile_dr(request):
    user = User.objects.get(id=request.user.id)
    dr_user = DrUser.objects.get(user=user)
    time_dr = DoctorTime.objects.all().filter(user=dr_user)
    context = {
        "user": user,
        "dr_user": dr_user,
        'time_dr': time_dr,
    }
    return render(request, 'account/profile_dr.html', context)


@login_required()
def edit_dr(request):
    return render(request, 'account/edit_user.html')


@login_required()
def status_dr_time(request):
    user = User.objects.get(id=request.user.id)
    dr_user = DrUser.objects.get(user=user)
    time_dr = DoctorTime.objects.all().filter(user=dr_user)
    context = {
        'time_dr': time_dr,
    }
    return render(request, 'account/status_dr_time.html', context)


@login_required()
def status_dr_time(request):
    user = User.objects.get(id=request.user.id)
    time_sick = DoctorTime.objects.all().filter(sick_name=user)

    context = {
        'time_sick': time_sick,
    }
    return render(request, 'account/status_sick_time.html', context)
