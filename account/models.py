from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, national_code, password=None, **extra_fields):
        if not national_code:
            raise ValueError('you must provide a valid phone number')
        user = self.model(national_code=national_code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, national_code, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is superuser must have is_superuser=True.')

        return self.create_user(national_code, password, **extra_fields)


class User(AbstractUser):
    username = None
    USER_TYPE_CHOICES = (
        (1, 'DrUser'),
        (2, 'SickUser'),
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    national_code = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=11)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)
    objects = UserManager()

    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DrUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dr_user')
    specialization = models.CharField(max_length=150)
    address = models.TextField()
    system_number = models.CharField(max_length=5)
    office_number = models.CharField(max_length=11)
    profile_pic = models.ImageField(upload_to='media/profile_pics_Dr', blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


class SickUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sick_user')
    profile_pic = models.ImageField(upload_to='media/profile_pics_sick', blank=True, null=True)

    def __str__(self):
        return f"{self.user}"
