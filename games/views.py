from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from games.forms.game_form import GameCreateForm, GameUpdateForm, BuyGameForm
from games.models import Games, GamesImage, Order, OrderItem

from user.models import UserInfo

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

def mainpage(request):
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'mainpage/index.html', context)


def get_games_by_id(request, id):
    return render(request, 'games/games_details.html', {
        'games': get_object_or_404(Games, pk=id)
    })


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
def delete_game(request, id):
    game = get_object_or_404(Games, pk=id)
    game.delete()
    return redirect('games-index')


@user_passes_test(lambda u: u.is_superuser)
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

'''
@login_required
def buy_game(request, id):
    instance = get_object_or_404(UserInfo, pk=id)
    if request.method == 'POST':
        form = BuyGameForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('games_details', id=id)
    else:
        form = BuyGameForm(instance=instance)
    return render(request, 'games/buy_game.html', {
        'form': form,
        'id': id
    })
'''
@login_required
def buy_game(request, id):
    if request.method == 'POST':
        form = BuyGameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('games_details', id=id)
    else:
        form = BuyGameForm()
    return render(request, 'games/buy_game.html', {
        'form': form,
        'id': id
    })



'''
def add_to_cart(request, slug):
    game = get_object_or_404(Games, slug=slug)
    order_item = OrderItem.objects.create(game=game)
    order_set = Order.objects.filter(user=request.user, ordered=False)
    if order_set.exists():
        order = order_set[0]
        if order.games.filter(game__slug=game.slug).exist():
            order_item
'''