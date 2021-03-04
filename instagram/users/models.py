from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField()
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    site = models.URLField(max_length=228, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
