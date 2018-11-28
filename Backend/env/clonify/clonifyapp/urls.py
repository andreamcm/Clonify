from django.urls import path
from . import views
urlpatterns = [
    path('api/friend/', views.FriendListCreate.as_view() ),
    path('api/friends/', views.FriendsListCreate.as_view() ),
    path('api/album/', views.AlbumListCreate.as_view() ),
    path('api/genre/', views.GenreListCreate.as_view() ),
    path('api/song/', views.SongListCreate.as_view() ),
    path('api/artist/', views.ArtistListCreate.as_view() ),
    path('api/playlist/', views.PlaylistListCreate.as_view() ),
    path('api/playlists/', views.PlaylistsListCreate.as_view() ),
    path('api/lastsong/', views.LastSongListCreate.as_view() ),

]