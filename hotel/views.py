from django.shortcuts import render
from django.contrib import messages
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
    adult = request.GET.get('adult')
    childred = request.GET.get('childred')
    context = {
        'hotel': hotel,
        'room_type': room_type,
        'rooms': rooms,
        'checkin': checkin,
        'checkout': checkout,
        'adult': adult,
        'children': children,
    }
    return render(request, 'hotel/room_type_detail.html', context)

def selectd_rooms(request):
    total = 0
    room_count = 0
    total_days = 0
    adult = 0
    children = 0
    checkin = 0
    checkout = 0

    if 'selected_data_obj' in request.session:
        for h_id, item in request.session['selection_data_obj'].items():
            print(h_id, item)
    else:
        message.warning