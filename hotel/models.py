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

ICON_TYPE = (
    ('Bootstrap Icons', 'Bootstrap Icons')
    ('Fontawsome Icons', 'Fontawsome Icons')
    ('Box Icons', 'Box Icons')
    ('Remi Icons', 'Remi Icons')
    ('Flat Icons', 'Flat Icons')
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
    image = models.FileField(upload_to='hotel_gallery')
    hgid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet='abcdefghijklmnopqrstuvwxyz')

    class Meta:
        verbose_name_plural = 'Hotel Gallery'

    def __str__(self):
        return self.hotel.name
    

class HotelFeature(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    icon_type = models.CharField(max_length=100, null=True, blank=True, choices=ICON_TYPE)
    icon = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Hotel Features'

    def __str__(self):
        return self.name


class HotelFaqs(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Hotel FAQs'

    def __str__(self):
        return self.question


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=2, decimal_places=2, default=0.00)
    number_of_beds = models.PositiveIntegerField(default=0)
    room_capacity = models.PositiveIntegerField(default=0)
    rtid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet='abcdefghijklmnopqrstuvwxyz')
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Room Types'

    def __str__(self):
        return f'{self.type} - {self.hotel.name} - {self.price}'

    def save(self, *args, **kwargs):
        if self.slug == '' or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.hotel.name) + '-' + str(uniqueid).lower()
            super(RoomType, self).save(*args, **kwargs)
    
    def rooms_count(self):
        Room.objects.filter(room_type=self).count()

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)