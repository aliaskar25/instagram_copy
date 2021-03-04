import uuid
import os

from django.db import models

from users.models import User


def upload_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)
    

class Post(models.Model):
    title = models.CharField(max_length=228)
    description = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')



class PostImage(models.Model):
    image = models.ImageField(upload_to=upload_image)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

