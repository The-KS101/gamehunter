from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('similarGames/<str:game>/filter?<str:console>', views.simGames, name="similar_games"),
    path('similar-games-json/<str:game>/filter?<str:console>', views.simGamesJson, name='sim_games_json'),
    path('games-json', views.gameListJson, name='sim_games_json'),
    path('similarGames/<str:game>/filter?<str:console>/sort?<str:sortBy>&<str:ordChoice>', views.simGamesSorted, name="similar_games_sorted"),
]
