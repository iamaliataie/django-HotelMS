from django.urls import path

urlpatterns = [
    path('register/', VIEW.as_view(), name=''),
]