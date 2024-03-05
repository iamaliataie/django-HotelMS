from django.shortcuts import render, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def check_room_availability(request):
    if request.method == 'POST':
        id = request.POST.get('hotel-id')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        adult = request.POST.get('adult')
        children = request.POST.get('children')
        room_type = request.POST.get('room_type')

        hotel = Hotel.objects.get(id=id)
        room_type = RoomType.objects.get(hotel=hotel, slug=room_type)

        url = reverse('hotel:room_type_detail', args=[hotel.slug, room_type.slug])
        url_with_params = f'{url}?hotel-id={id}&checkin={checkin}&checkout={checkout}&adult={adult}&children={children}'
        return HttpResponseRedirect(url_with_params)

def add_to_selection(request):
    room_selection = {}
    room_selection[str(request.GET['id'])] = {
        'hotel_id': request.GET['hotel_id'],
        'hotel_name': request.GET['hotle_name'],
        'room_name': request.GET['room_name'],
        'room_price': request.GET['room_price'],
        'number_of_beds': request.GET['number_of_beds'],
    }