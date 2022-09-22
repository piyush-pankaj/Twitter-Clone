from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class post (models.Model):
    class Meta(object):
        db_table= 'post'

    name=models.CharField(
        'name', blank=False, null= False, max_length=14, db_index=True, default='Anonymous'
    )

    body = models.CharField(
        'name', blank=True, null=True, max_length=140, db_index=True 
    )
    created_at =models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    likes= models.IntegerField(
        'likes', default=0, blank=True
    )
    image= CloudinaryField(
        'image', blank=True, db_index=True
    )