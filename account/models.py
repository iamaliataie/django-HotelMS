from django.db import models
from django.contrib.auth.models import AbstractUser

from shortuuid.django_fields import ShortUUIDField
# Create your models here.

GENDER = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Other', 'Other')
)

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.user.id}.{ext}'
    return f'user_{instance.user.id}/{filename}'

class User(AbstractUser):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=500, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='Other')
    otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD=['email']
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabets='abcdefghijklmnopqrstuvwxyz123')
    image = models.FileField(upload_to=user_directory_path, default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='Other')
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
