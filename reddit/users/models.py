from django.db import models
from django.utils import timezone


# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    mobile = models.CharField(max_length=12)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    profile_image = models.URLField(null=True)
    email = models.EmailField(null=True)
    posts = models.ManyToManyField('uploads.Posts', related_name='post_user')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
