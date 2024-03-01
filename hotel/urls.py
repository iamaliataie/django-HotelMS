from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<slug>/', views.hotel_detail, name='hotel_detail'),
    path('detail/', VIEW.as_view(), name=''),
]