from typing_extensions import Required
from django.db import models

# Create your models here.

class Songs(models.Model):
    title = models.CharField()
    