from django.contrib import admin
from .models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType, HotelGallery


class HotelGalleryInline(admin.TabularInline):
    model = HotelGallery

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelGalleryInline]
    list_display = ['thumbnail', 'name', 'user', 'status']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)
