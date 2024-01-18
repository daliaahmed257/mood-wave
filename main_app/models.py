from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.



class Mood(models.Model):
  title = models.CharField()
  description = models.TextField()

class Song(models.Model):
  title = models.CharField()
  artist = models.CharField()
  mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
  mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
  mp3_file = models.FileField(upload_to='mp3_files/')
  Hyperlink = models.CharField(max_length=200)

class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_("email address"), unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  date_joined = models.DateTimeField(default=timezone.now)
  favorites = models.ManyToManyField(Song, default=list)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email

class Journal(models.Model):
  content = models.TextField(default="")
  date = models.DateTimeField(timezone.now)
  user = models.ForeignKey(CustomUser)
class Journal(models.Model):
  content = models.TextField(default="")
  date = models.DateTimeField(timezone.now)
  user = models.ForeignKey(CustomUser)


