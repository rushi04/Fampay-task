from django.db import models
from datetime import datetime

# Create your models here.
    
class Channel(models.Model):
    class Meta:
        ordering=['channelId']

    channelId = models.CharField(primary_key = True,db_index=True, max_length = 100)
    channelTitle = models.TextField()


class Video(models.Model):
    class Meta:
        ordering=['-publishedAt']

    videoId = models.CharField(primary_key = True,max_length=150, blank=True)
    title = models.TextField()
    description = models.TextField()
    publishedAt = models.DateTimeField(default=datetime.now, db_index=True, blank=True)
    thumbnail = models.TextField(blank = True)
    channelId = models.CharField(max_length = 100,blank = True)


