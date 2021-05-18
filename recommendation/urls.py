from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('similarGames/<str:game>/filter?<str:console>', views.simGames, name="similar_games"),
    # path('similarGames/<str:game>/filter?<str:console>/sort?<str:sortBy>&<str:ordChoice>', views.simGamesSorted, name="similar_games_sorted"),
]
