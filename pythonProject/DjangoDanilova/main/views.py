import datetime

from django.shortcuts import render
from django.http import HttpResponse
from random import choice
import datetime

# def one(request):
#         quotes = ['Добро пожаловать', 'До свидания', 'Пока']
#         # return HttpResponse(f'<h1><center>{choice(quotes)}<center></h1>')
#         return render(request, 'main/index.html')
# def two(request):
#         return HttpResponse(f'<h1>{(datetime.timedelta(256) + datetime.datetime(2024, 1, 1))}<h1>')
#
# massive = []
#
# for i in range(1, 10):
#         for j in range(1, 10):
#                 massive.append(f'{i * j}')
#
# def lol(request):
#         return HttpResponse(f'<p>{[i for i in massive]}</p>')
#
# def about(request):
#         return HttpResponse('<h2>О нас!</h2>')

# def main(request):
#         return HttpResponse('<style>h1 {color: red; font-weight: 100px;}</style><h1><center>Главная<center></h1>')
#
# def news(request):
#         return HttpResponse('<h1><center>Новости<center></h1>')
#
# def about(request):
#         return HttpResponse('<h1><center>О компании<center></h1>')
#
# def contacts(request):
#         return HttpResponse('<h1><center>Контакты<center></h1>')


def main(request):
        return render(request, 'index.html')
        # return HttpResponse('<style>body {background-color: white;} h1 {color: blue; font-size: xxx-large; margin-top: 400px;}</style><h1><center>Главная<center></h1>')


def z_age(request, age):
        if age >= 12 and age <= 27:
                return HttpResponse('<style>h1 {color: green; font-size: xxx-large; margin-top: 400px;}</style><h1><center>Зумер<center></h1>')
        if age >= 28 and age <= 43:
                return HttpResponse('<style>body {background-color: black;} h1 {color: red; font-size: xxx-large; margin-top: 400px;}</style><h1><center>Доступ запрещен<center></h1>')
        if age < 12 or age > 43:
                return HttpResponse(
                        '<style>body {background-color: white;} h1 {color: blue; font-size: xxx-large; margin-top: 400px;}</style><h1><center>Главная<center></h1>')


def m_age(request, age):
        if age >= 28 and age <= 43:
                return HttpResponse('<style>h1 {color: green; font-size: xxx-large; margin-top: 400px;}</style><h1><center>Миллениал<center></h1>')
        if age >= 12 and age <= 27:
                return HttpResponse('<style>body {background-color: black;} h1 {color: red; font-size: xxx-large; margin-top: 400px;}</style><h1><center>Доступ запрещен<center></h1>')
        if age < 12 or age > 43:
                return HttpResponse(
                        '<style>body {background-color: white;} h1 {color: blue; font-size: xxx-large; margin-top: 400px;}</style><h1><center>Главная<center></h1>')

