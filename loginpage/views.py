from django.shortcuts import render
#from games.models import Games
# Create your views here
def index(request):
    return render(request, 'loginpage/index.html')
