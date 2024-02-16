from django.shortcuts import render


from account.models import User, Profile
from account.forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm()
    
    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)