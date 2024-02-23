from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
import shortuuid
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
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=20, choices=HOTEL_STATUS, default='live')
    tags = models.CharField(max_length=200, help_text='Seperate tags with commas')
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    hid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet='abcdefghijklmnopqrstuvwxyz')
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '' or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqeid = uuid_key[:4]
            self.slug = slugify(self.name) + '-' + str(uniqeid)
        super(Hotel, self).save(*args, **kwargs)

    def thumbnail(self):
        return mark_safe(f"<img src='{self.image.url}' width='50px' height='50px' style='object-fit:cover; border-radius:6px;' />")


class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)