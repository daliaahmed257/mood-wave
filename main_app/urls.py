from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('moods/', views.moods_index, name='index'),
  path('playlists/', views.playlists, name='playlists'),
  path('moods/create', views.CreateMood.as_view(), name='create'),
  path('moods/<int:mood_id>/update/', views.MoodUpdate.as_view(),name='moods_update'),
  path('moods/<int:mood_id>/delete/',views.MoodDelete.as_view(),name='moods_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('logout/', views.user_logout, name='logout'),
  path('moods/<int:mood_id>/', views.moods_detail, name='detail'),
  path('moods/<int:mood_id>/song_file/', views.song_file, name='song_file')
]
