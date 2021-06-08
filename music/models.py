from django.db import models

# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000,  null=True)
    artist = models.CharField(max_length=2000,  null=True)
    tags = models.CharField(max_length=2000,  null=True)
    thumbnail = models.ImageField(upload_to="", null=True)
    songs = models.FileField(upload_to="",  null=True)


    def __str__(self):
        return self.name
