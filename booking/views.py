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

def check_room_availability(request):
    if request.method == 'POST':
        id = request.POST.get('hotel-id')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        adult = request.POST.get('adult')
        children = request.POST.get('children')
        room_type = request.POST.get('room_type')
