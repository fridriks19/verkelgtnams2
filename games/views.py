from django.shortcuts import render
from games.models import Games
# Create your views here
def index(request):
    context = {'games': Games.objects.all().order_by('name') }
    return render(request, 'games/index.html', context)
