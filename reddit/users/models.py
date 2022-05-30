from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as DefaultUser
from utils.models import TimeStampModel
# Create your models here.


class User(DefaultUser, TimeStampModel):
    mobile = models.CharField(max_length=12)
    profile_image = models.URLField(null=True)
    posts = models.ManyToManyField('uploads.Posts', related_name='post_user')

