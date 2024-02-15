from django.contrib import admin
from .models import User, Profile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'username']
    list_display = ['username', 'full_name', 'email', 'phone', 'gender']

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'user__username']
    list_display = ['full_name', 'user', 'verified']

admin.site.regiser(User, UserAdmin)
admin.site.regiser(Profile, ProfileAdmin)