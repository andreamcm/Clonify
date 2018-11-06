from rest_framework import serializers
from clonifyapp.models import *

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '_all_'

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '_all_'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '_all_'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '_all_'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '_all_'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '_all_'

class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = '_all_'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '_all_'

class LastSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastSong
        fields = '_all_'