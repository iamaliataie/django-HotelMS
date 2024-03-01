from django.shortcuts import render
from .models import Hotel, Booking, ActivityLog, RoomType, Room

# Create your views here.

def index(request):
    hotels = Hotel.objects.filter(status='live')
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/index.html', context)

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(status='live', slug=slug)
    context = {
        'hotel': hotel
    }
    return render(request, 'hotel/hotel_detail.html', context)

def room_detail(request, slug, rt_slug):
    hotel = Hotel.objects.get(status='live', slug=slug)
    room_type = RoomType.objects.get(hotel=hotel, slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)

    context = {
        'hotel': hotel,
        'room_type': room_type,
        'rooms': rooms
    }

    return render(request)