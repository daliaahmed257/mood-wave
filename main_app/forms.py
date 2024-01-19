from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Song

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ("email",)

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'Hyperlink']