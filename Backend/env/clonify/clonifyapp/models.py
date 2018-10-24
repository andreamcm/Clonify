from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User model

# Friend model
class Friend(models.Model):
    friendId = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

# Friends model
class Friends(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

# Albums model
class Album(models.Model):
	name = models.CharField(max_length=50)
	img = models.CharField(max_length=900)


# Genres model
class Genre(models.Model):
	name = models.CharField(max_length=50)


# Songs model
class Song(models.Model):
	title = models.CharField(max_length=100)
	artistaId = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	albumId = models.ForeignKey(Album, null=True, on_delete=models.CASCADE)
	genreId = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE)


# Artist model
class Artist(models.Model):
	name = models.CharField(max_length=50)
	img = models.CharField(max_length=900)


# Playlist model
class Playlist(models.Model):
	name = models.CharField(max_length=50)
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


# Song playlist model
class SongPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)


# Last song played (optional)
