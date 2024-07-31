import random

from django.shortcuts import render

# Create your views here.

def about(request):
    text = random.randint(0, 10)
    gen = [i for i in range(10)]
    cont = {
        'title':'О нас',
        'text': text,
        'gen': gen
    }
    return render(request, 'about.html', cont)

def about_digite(request, digite):
    text = random.randint(0, 10)
    cont = {
        'title':'О нас',
        'text': text,
        'digite': digite
    }
    return render(request, 'about.html', cont)