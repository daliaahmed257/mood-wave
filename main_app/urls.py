from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('moods/', views.moods_index, name='index'),
  path('playlists/', views.playlists, name='playlists'),
  path('moods/', views.moods_create, name='create'),
  path('accounts/signup/', views.signup, name='signup'),
  path('logout/', views.user_logout, name='logout'),
  path('moods/<int:mood_id>/add_song/', views.add_song, name='add_song')
]
