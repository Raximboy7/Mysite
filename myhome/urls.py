from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.BASE, name='BASE'),
    path('home/',views.Home, name='Home')
]
