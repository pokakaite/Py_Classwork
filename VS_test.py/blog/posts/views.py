from django.shortcuts import render
from .models import Posts

# Create your views here.

def index(request):
    posts = Posts.objects.all()
    context = {
        'posts':posts
    }
    # if request.GET:
    #     found = request.GET['name']
    #     context.update({'found':found})

    return render(request, 'posts/index.html', context)

# def smth(request, smth):
#     cont = {
#         'smth':smth,
#     }
#     return render(request, 'posts/smth.html', cont)

def create(request):
    context = {}
    return render(request, 'posts/create.html', context)
