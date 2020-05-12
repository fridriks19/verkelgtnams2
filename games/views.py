from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from games.forms.game_form import GameCreateForm, GameUpdateForm
from games.models import Games, GamesImage


# Create your views here
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.gamesimage_set.first().image
        } for x in Games.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': games})
    context = {'games': Games.objects.all().order_by('name') }
    return render(request, 'games/index.html', context)


def get_games_by_id(request, id):
    return render(request, 'games/games_details.html', {
        'games': get_object_or_404(Games, pk=id)
    })
@login_required
def create_game(request):
    if request.method == 'POST':
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            game = form.save()
            game_image = GamesImage(image=request.POST['image'], games=game)
            game_image.save()
            return redirect('games-index')
    else:
        form = GameCreateForm()
    return render(request, 'games/create_game.html', {
        'form': form
    })
@login_required
def delete_game(request, id):
    game = get_object_or_404(Games, pk=id)
    game.delete()
    return redirect('games-index')
@login_required
def update_game(request, id):
    instance = get_object_or_404(Games, pk=id)
    if request.method == 'POST':
        form = GameUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('games_details', id=id)
    else:
        form = GameUpdateForm(instance=instance)
    return render(request, 'games/update_game.html', {
        'form': form,
        'id': id
    })
