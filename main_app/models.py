from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

MOOD_CHOICES = [
        ("HAPPY", "Happy"),
        ("CALM", "Calm"),
        ("SAD", "Sad"),
        ("BORED", "Bored"),
        ("ANXIOUS", "Anxious"),
        ("ANGRY", "Angry"),
    ]

class Song(models.Model):
  title = models.CharField()
  artist = models.CharField()
  Hyperlink = models.CharField()
  url = models.CharField(max_length=200)
  mood = models.CharField(max_length=7, choices=MOOD_CHOICES)
  def __str__(self):
        return self.title

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
  
class Mood(models.Model):
  title = models.CharField(max_length=7, choices=MOOD_CHOICES, verbose_name="How are you feeling?")
  content = models.TextField(default="", verbose_name="Could to explain further?")
  date = models.DateTimeField(default=timezone.now)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
  def __str__(self):
        return self.title
  
  def assign_color(self):
    match self.title:
       case "HAPPY":
          return "yellow"
       case "SAD":
          return "blue"
       case "ANGRY":
          return "red"
       case "ANXIOUS":
          return "black"
       case "CALM":
          return "green"
       case "BORED":
          return "brown"
  
  def get_absolute_url(self):
      return reverse("detail", kwargs={"mood_id": self.pk})
  
  
  
  


  
  
  



