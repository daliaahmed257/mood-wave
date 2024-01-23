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
  avatar = models.URLField(max_length=200, default="https://mood-wave-avatars.s3.us-east-2.amazonaws.com/e9090c.jpeg")

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
       if self.title == "HAPPY":
          return "#97F8C4"
       elif self.title == "SAD":
          return "#EDEF84"
       elif self.title == "ANGRY":
          return "#FE8392"
       elif  self.title == "ANXIOUS":
          return "#F4945E"
       elif self.title == "CALM":
          return "#97E1F8"
       elif self.title == "BORED":
          return "#90ADF9"
  
  def get_absolute_url(self):
      return reverse("detail", kwargs={"mood_id": self.pk})
  
  

  
  
  
  


  
  
  



