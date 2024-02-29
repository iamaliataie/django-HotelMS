from django.shortcuts import render
from .models import Hotel, Booking

# Create your views here.

def index(request):
    return render(request, 'hotel/index.html')