from django.shortcuts import render, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import render_to_string
from hotel.models import (
    Hotel, 
    Booking, 
    ActivityLog,
    HotelGallery,
    StaffOnDuty,
    Room,
    RoomType,
)


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
        'room_number': request.GET['number_of_beds'],
        'room_type': request.GET['room_type'],
        'room_id': request.GET['room_id'],
        'checkout': request.GET['checkout'],
        'checkin': request.GET['checkin'],
        'adult': request.GET['adult'],
        'children': request.GET['adult'],
    }
    
    if 'selection_date_obj' in request.session:
        if str(request.GET['id']) in request.session['selection_date_obj']:
            selection_date = request.session['selection_date_obj']
            selection_date[str(request.GET['id'])]['adult'] = int(room_selection[str(request.GET['id'])]['adult'])
            selection_date[str(request.GET['id'])]['children'] = int(room_selection[str(request.GET['id'])]['children'])
            request.session['selection_date_obj'] = selection_date
        else:
            selection_date = request.session['selection_date_obj']
            selection_date.update(room_selection)
            request.session['selection_date_obj'] = selection_date
    else:
        request.session['selection_date_obj'] = room_selection
        
    data = {
        'data': request.session['selection_date_obj'],
        'fruit': 'banana',
        'name': 'Ali Ahmad Ataie',
        'total_selected_items': request.session['selection_date_obj']
    }
    
    return JsonResponse(data)

def delet_selection(request):
    hotel_id = str(request.GET.get('id'))
    if 'selection_data_obj' in request.session:
        if hotel_id in request.session['selection_data.obj']:
            selection_data = request.session['selection_data_obj']
            del request.session['selection_data_obj'][hotel_id]
            request.session['selection_data_obj'] = selection_data
            
    total = 0
    total_day = 0
    room_count = 0
    adult = 0
    children = 0
    checkin = 0
    checkout = 0
    hotel = None
    
    if 'selection_data_obj' in request.session:
        for h_id, item in request.session['selection_data_obj'].items():
            id = int(item['hotel_id'])
            checkin = item['checkin']
            checkout = item['checkout']
            adult = int(item['adult'])
            children = int(item['children'])
            room_type = int(item['room_type'])
            room_id = int(item['room_id'])
            
            room_type = RoomType.objects.get(id=room_type)
            date_format = '%Y-%m-%d'
            checkin_date = datetime.strptime(checkin, date_format)
            checkout_date = datetime.strptime(checkout, date_format)
            time_difference = checkout_date - checkin_date
            total_days = time_difference.days
            
            room_count += 1
            days = total_days
            price = room_type.price
            room_price = price * room_count
            total = room_price * days

    context = render_to_string(
        'hotel/async/selected_room.html',
        {
            'data': request.session['selection_data_obj'],
            'total_selected_item': len(request.session['selection_data_obj']),
            'total': total,
            'total_days': total_days,
            'adult': adult,
            'children': children,
            'checkin': checkin,
            'checkout': checkout,
            'hotel': hotel,
        }
    )
    
    return JsonResponse(
        {
            'data': context,
            'total_selected_item': len(request.session['selection_data_obj']),
        }
    )
