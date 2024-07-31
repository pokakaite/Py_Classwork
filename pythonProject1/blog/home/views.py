import datetime

from django.shortcuts import render

# Create your views here.

def home(request):
    cont = {
        'title':'Главная',
        'time': datetime.datetime.now()
    }
    return render(request, 'home.html', cont)
