from django.shortcuts import render
from .models import Hotel, Booking, ActivityLog

# Create your views here.

def index(request):
    hotels = Hotel.objects.filter(status='live')
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/index.html', context)

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(status='live', slug=slug)