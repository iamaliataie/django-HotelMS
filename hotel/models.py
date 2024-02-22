from django.db import models
from shortuuid.django_fields import ShortUUIDField
from account.models import User
# Create your models here.

HOTEL_STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('live', 'Live')
)

class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='hotel_gallery')
    address = models.CharField(max_length==200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=20, choices=HOTEL_STATUS, default='live')
    tags = models.CharField(max_length=200, help_text='Seperate tags with commas')
    views = models.IntegerField(default=0)
    featured = models.BooleanField()