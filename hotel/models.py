from django.db import models
from account.models import User
# Create your models here.

class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.TextField()