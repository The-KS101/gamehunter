from os import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('similarGames/<str:game>/filter?<str:console>', views.simGames, name="similar_games"),
    path('similar-games-json/<str:game>/filter?<str:console>', views.simGamesJson, name='sim_games_json'),
    path('games-json', views.gameListJson, name='sim_games_json'),
    path('featured_games', views.featured_games, name='featured_games'),
    path('about', views.about, name='about'),
]
