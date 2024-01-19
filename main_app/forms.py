from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Song

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ("email",)

class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ['mood']