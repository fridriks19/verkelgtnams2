from django.urls import path
from . import views
urlpatterns = [
    path('get_games_by_highest', views.get_games_by_highest, name="game_highest"),
    path('get_games_by_lowest', views.get_games_by_lowest, name="game_lowest"),
    path('get_games_by_name', views.get_games_by_name, name="game_name"),
    path('get_games_by_category', views.get_games_by_category, name="game_category"),
    path('get_games_by_console', views.get_games_by_console, name="game_console"),
    path('', views.index, name="games-index"),
    path('<int:id>', views.get_games_by_id, name="games_details"),
    path('create_game', views.create_game, name="create_game"),
    path('delete_game/<int:id>', views.delete_game, name='delete_game'),
    path('update_game/<int:id>', views.update_game, name="update_game"),
    path('buy_game/<int:id>', views.buy_game, name="buy_game"),
    path('payment_info/<int:id>', views.payment_info, name="payment_info"),
]