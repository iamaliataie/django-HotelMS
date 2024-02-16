from django.shortcuts import render
from django.contrib.auth import authenticate

from account.models import User, Profile
from account.forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm()
    
    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)