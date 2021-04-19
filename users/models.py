from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No bio yet...')
    image = models.ImageField(upload_to='profiles', default='avatar.png')


    def __str__(self):
        return f'{self.user.username} Profile'

