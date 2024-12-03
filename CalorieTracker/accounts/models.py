# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    objects = models.Manager()  # This is not needed, it’s automatically provided by Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100, blank=True, default="User")  # Custom identifier
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profile_pics/', blank=True)
    calorie_goal = models.IntegerField(default=2000)

    def __str__(self):
        return self.profile_name  # Use the custom profile name field




#objects = models.Manager()  # This is not needed, it’s automatically provided by Django