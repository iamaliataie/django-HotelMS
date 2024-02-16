from django.shortcuts import render


from account.models import User, Profile
from account.forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm()
    
    if form.is_valid():

    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)