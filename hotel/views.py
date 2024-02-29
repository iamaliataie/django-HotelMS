from django.shortcuts import render
from .models import Hotel, Booking, ActivityLog

# Create your views here.

def index(request):
    hotels = Hotel
    return render(request, 'hotel/index.html')