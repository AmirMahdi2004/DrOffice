from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reserv', views.reservation, name='reservation'),
    path('verifi/<pk>', views.verifi_reservation, name='verifi'),
    path('create_reservation/', views.create_reservation, name='create_reservation')
]
