from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from account.models import User, Profile
from account.forms import UserRegistrationForm
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in.')
        return redirect('hotel:home')
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(email=email, password=password)
        login(request, user)
        messages.success(request, f'Hey {full_name}, your account has been created succussfully.')

        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()
        return redirect('hotel:home')

    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are logged in.')
        return redirect('hotel:home')
    
    if request.method == 'POST':
        email = request.POST.get('email')