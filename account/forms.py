from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class DrSUserCreationsForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('national_code', 'phone_number', 'last_name', 'first_name', 'is_active', 'is_staff', 'user_type')


class DrCUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('national_code', 'phone_number', 'last_name', 'first_name', 'is_active', 'is_staff', 'user_type')


class DrRegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='repeat password')

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'national_code', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1
        if commit:
            user.save()
        return user


class SickRegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='repeat password')

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'national_code', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['national_code', 'password']
