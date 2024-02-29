from django.contrib import admin
from .models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType, HotelGallery
# Register your models here.


class HotelGalleryInline(admin.TabularInline):
    model = HotelGallery

class HotelAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ['thumbnail', 'name', 'user', 'status']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)