from django.shortcuts import render

# Create your views here.

def index(request):
    if request.GET:
        found = request.GET['name']
        context = {
            'found':found
        }
        return render(request, 'posts/index.html', context)
    else:
        context={}
        return render(request, 'posts/index.html')

def smth(request, smth):
    cont = {
        'smth':smth,
    }
    return render(request, 'posts/smth.html', cont)
