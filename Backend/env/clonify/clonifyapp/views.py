from clonifyapp.models import *
from clonifyapp.serializers import *
from rest_framework import generics

class FriendListCreate(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FriendsListCreate(generics.ListCreateAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer
  
class AlbumListCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtistListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class PlaylistListCreate(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistsListCreate(generics.ListCreateAPIView):
    queryset = Playlists.objects.all()
    serializer_class = PlaylistsSerializer

class LastSongListCreate(generics.ListCreateAPIView):
    queryset = LastSong.objects.all()
    serializer_class = LastSongSerializer