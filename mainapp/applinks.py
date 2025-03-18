from .views import fetch_all_movies_page, fetch_one_movie_page, fetch_one_player_page, loginpage, homepage, moviepage, fetch_all_players_page, update_one_movie, update_one_player, delete_one_player
from django.urls import path
urlpatterns = [
    path("homepage/", homepage, name="homepage"),
    path("loginpage/", loginpage, name="loginpage"),
    path("moviepage/", moviepage, name="moviepage"),
    path("allplayerspage/", fetch_all_players_page, name="allplayerspage"),
    path("allmoviespage/", fetch_all_movies_page, name="allmoviespage"),
    path("oneplayerpage/<int:pk>", fetch_one_player_page, name="oneplayerpage"),
    path("onemoviepage/<int:pk>", fetch_one_movie_page, name="onemoviepage"),
    path("updateplayerpage/<int:pk>", update_one_player, name="updateplayerpage"),
    path("updatemoviepage/<int:pk>", update_one_movie, name="updatemoviepage"),
    path("delete_one_player/<int:pk>", delete_one_player, name="deleteoneplayer")
]