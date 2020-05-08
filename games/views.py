from django.shortcuts import render, get_object_or_404

from games.forms.game_form import GameCreateForm
from games.models import Games
# Create your views here
def index(request):
    context = {'games': Games.objects.all().order_by('name') }
    return render(request, 'games/index.html', context)

def get_games_by_id(request, id):
    return render(request, 'games/games_details.html', {
        'games': get_object_or_404(Games, pk=id)
    })

def create_game(request):
    if request.method == 'POST':
        print(1)
    else:
        form = GameCreateForm()
    return render(request, 'games/create_game.html', {
        'form': form
    })

