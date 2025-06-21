from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    id_user=models.CharField(max_length=100)
    bio=models.TextField()
    profileimg=models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username


class post(models.Model):
    id= models.UUIDField(primary_key=True)
    user= models.CharField(max_length=100)
    image= models.ImageField(upload_to='post_images')
    caption= models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user