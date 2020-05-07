from django.shortcuts import render
from computers.models import Computers
# Create your views here
def index(request):
    context = {'computers': Computers.objects.all().order_by('name') }
    return render(request, 'computers/index.html', context)
