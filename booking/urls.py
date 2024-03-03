from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path(
        'check_room_availability/',
        VIEW.as_view(),
        name=''
    ),
]