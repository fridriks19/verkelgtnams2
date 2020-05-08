from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="games-index"),
    path('<int:id>', views.get_games_by_id, name="games_details"),
    path('create_game', views.create_game, name="create_game")
]