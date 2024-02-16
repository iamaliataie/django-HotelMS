from django.shortcuts import render
from account.models import User, Profile
from account.forms import UserRegistrationForm
# Create your views here.

def RegisterView(request):
    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'account/signup.html', context)