from django.db import models

# Create your models here.
from django.db.models import CharField


class Video(models.Model):
    video_path = CharField(max_length=200)
    video_name = CharField(max_length=200)
    video_summary = CharField(max_length=500, null=True)