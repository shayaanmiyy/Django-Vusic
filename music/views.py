from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

# Create your views here.
def index(request):
    song = Song.objects.all()
    return render(request, 'home.html', {'song' : song})

def allsongs(request):
    song = Song.objects.all()
    return render(request, 'allsongs.html', {'song' : song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'songpost.html', {'song' : song})

def search(request):
    query = request.GET['search']
    search = Song.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'search' : search})


