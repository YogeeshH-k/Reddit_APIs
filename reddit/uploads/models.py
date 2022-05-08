from django.db import models
from django.utils import timezone
# Create your models here.


class Posts(models.Model):
    url = models.URLField(null=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

