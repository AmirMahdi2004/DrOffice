from django.urls import path
from account import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register_dr', views.register_dr, name='register_dr'),
    path('profile_dr', views.profile_dr, name='profile_dr'),
    path('register_user', views.register_user, name='register_user'),
    path('profile_user', views.profile_user, name='profile_user'),
    path('edit_dr', views.edit_dr, name='edit_dr'),
    path('status', views.status_dr_time, name='status'),
]
