from django.db import models
from django.contrib.auth.models import User # it have-email,pass,username,first,last name
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Inheriting built in User class

    # extending User class
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username