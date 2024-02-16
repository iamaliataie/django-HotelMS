from django.urls import path
from . import views
urlpatterns = [
    path('register/', VIEW.as_view(), name=''),
]