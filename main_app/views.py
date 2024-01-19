import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mood, Song, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def moods_index(request):
  songs=Song.objects.all()
  moods=Mood.objects.filter(user = request.user.id)
  print(request.user.id)
  return render(request, 'moods/index.html', {
    'songs' : songs,
    'moods': moods
  })

@login_required
def playlists(request):
  return render(request, 'playlists.html')

class CreateMood(CreateView):
  model = Mood
  fields = ["title", "content"]
  
class MoodUpdate(UpdateView):
  model = Mood
  fields = [ 'title', 'content']
  
class MoodDelete(DeleteView):
  model = Mood
  success_url = '/moods'
  


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = CustomUserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def user_logout(request):
    if request.method == 'POST':
        # Log the user out
        logout(request)
        # Redirect to the home page or any other desired page
        return redirect('home')
    # If it's a GET request, you can handle it differently or just redirect to home
    # Log the user out
    logout(request)
    return redirect('home')
  
  
def moods_detail(request, mood_id):
  mood= Mood.objects.get(id=mood_id)
  songs = Song.objects.filter(mood= mood)
  song = songs[random.randint(0, songs.count()-1)]
  return render(request, 'moods/detail.html', {'mood' :mood, 'song': song})
  
  
  



