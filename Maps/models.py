from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Search(models.Model):
    Origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_searched= models.DateTimeField(default=timezone.now)
    metric=models.BooleanField(default=False)