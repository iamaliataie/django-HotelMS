from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Other', 'Other')
)

class User(AbstractUser):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=500, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='Other')
    otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD=['email']