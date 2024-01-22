from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('user/<int:user_id>', views.user_detail, name="user_page"),
  path('user/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),
  path('about/', views.about, name='about'),
  path('moods/', views.moods_index, name='index'),
  path('playlists/', views.playlists, name='playlists'),
  path('moods/create', views.CreateMood.as_view(), name='create'),
  path('moods/<int:pk>/update/', views.MoodUpdate.as_view(),name='moods_update'),
  path('moods/<int:pk>/delete/',views.MoodDelete.as_view(),name='moods_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('logout/', views.user_logout, name='logout'),
  path('moods/<int:mood_id>/', views.moods_detail, name='detail'),
  path('moods/<int:mood_id>/song_file/', views.song_file, name='song_file'),
  path('playlists/happy/', views.happy_playlist, name='happy_playlist'),
  path('playlists/sad/', views.sad_playlist, name='sad_playlist'),
  path('playlists/angry/', views.angry_playlist, name='angry_playlist'),
  path('playlists/calm/', views.calm_playlist, name='calm_playlist'),
  path('playlists/bored/', views.bored_playlist, name='bored_playlist'),
  path('playlists/anxious/', views.anxious_playlist, name='anxious_playlist'),
  path('add_song/<int:mood_id>/', views.add_song, name='add_song'),
  path('delete_song/<int:song_id>/<str:playlist>/', views.delete_song, name='delete_song'),
  path('edit_song/<int:song_id>/<str:playlist>/', views.edit_song, name='edit_song'),
  path('moods/<int:mood_id>/add_moodphoto/', views.add_moodphoto, name='add_moodphoto'),
]