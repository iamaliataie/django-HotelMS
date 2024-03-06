from django.shortcuts import render
from .models import Hotel, Booking, ActivityLog, RoomType, Room


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

def room_type_detail(request, slug, rt_slug):
    hotel = Hotel.objects.get(status='live', slug=slug)
    room_type = RoomType.objects.get(hotel=hotel, slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)

    id = request.GET.get('hoted-id')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')

    return render(request, 'hotel/room_type_detail.html', context)
