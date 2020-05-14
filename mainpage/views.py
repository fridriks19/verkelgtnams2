from django.shortcuts import render

from computers.models import Computers
from games.models import Games
# Create your views here
def index(request):
    context = {'games': Games.objects.all().order_by('name'), 'computers': Computers.objects.all().order_by('name')}
    return render(request, 'mainpage/index.html', context)






