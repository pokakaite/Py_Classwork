from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', about, name='about'),
    path('<int:digite>/', about_digite, name='about_digite'),
]