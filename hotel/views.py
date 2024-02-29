from django.shortcuts import render
from .models import Hotel

# Create your views here.

def index(request):
    return render(request, 'hotel/index.html')