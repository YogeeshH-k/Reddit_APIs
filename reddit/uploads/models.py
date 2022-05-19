from django.db import models
from utils.models import TimeStampModel
from django.utils import timezone
# Create your models here.


class Posts(TimeStampModel):
    url = models.URLField(null=True)
    description = models.TextField()

