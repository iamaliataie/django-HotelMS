from django.shortcuts import render, render, redirect
from django.urls import reverse
from hotel.models import (
    Hotel, 
    Booking, 
    ActivityLog,
    HotelGallery,
    StaffOnDuty,
    Room,
    RoomType,
)
# Create your views here.
