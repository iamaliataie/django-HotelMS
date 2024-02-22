from django.db import models
from account.models import User
# Create your models here.

class Hotel(models.Model):
    user = models.ForeignKey()