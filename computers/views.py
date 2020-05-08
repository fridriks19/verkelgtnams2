from django.shortcuts import render
from computers.models import Computers
# Create your views here
def index(request):
    context = {'computers': Computers.objects.all()}
    return render(request, 'computers/index.html', context)
