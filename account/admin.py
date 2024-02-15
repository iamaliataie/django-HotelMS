from django.contrib import admin
from .models import User, Profile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'username']