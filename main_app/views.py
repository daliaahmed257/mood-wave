from django.shortcuts import render
from .models import Song
# Create your views here.
def home(request):
  songs = Song.objects.all()
  print(songs)
  return render(request, 'home.html', {'songs': songs})




