from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.lol),
    path('about', views.about)
]


