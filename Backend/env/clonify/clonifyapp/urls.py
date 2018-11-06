from django.urls import path
from . import views
urlpatterns = [
    path('api/lead/', views.FriendListCreate.as_view() ),
    path('api/lead/', views.FriendsListCreate.as_view() ),
    path('api/lead/', views.AlbumListCreate.as_view() ),
    path('api/lead/', views.GenreListCreate.as_view() ),
    path('api/lead/', views.SongListCreate.as_view() ),
    path('api/lead/', views.ArtistListCreate.as_view() ),
    path('api/lead/', views.PlaylistListCreate.as_view() ),
    path('api/lead/', views.PlaylistsListCreate.as_view() ),
    path('api/lead/', views.LastSongListCreate.as_view() ),
]