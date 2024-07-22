import datetime

from django.shortcuts import render
from django.http import HttpResponse
from random import choice
import datetime


# Create your views here.


def one(request):
        quotes = ['Добро пожаловать', 'До свидания', 'Пока']
        return HttpResponse(f'<h1><center>{choice(quotes)}<center></h1>')

def two(request):
        return HttpResponse(f'<h1>{(datetime.timedelta(256) + datetime.datetime(2024, 1, 1))}<h1>')

massive = []

for i in range(1, 10):
        for j in range(1, 10):
                massive.append(f'{i * j}')

def lol(request):
        return HttpResponse(f'<p>{[i for i in massive]}</p>')

def about(request):
        return HttpResponse('<h2>О нас!</h2>')