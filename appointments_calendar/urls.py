from django.urls import path

from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('booked', views.book, name='book')
]