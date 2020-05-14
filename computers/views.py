
from computers.models import Computers
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        computers = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.computersimage_set.first().image,
            'price': x.price,
            'on_sale': x.on_sale,
            'discount_price': x.discount_price
        } for x in Computers.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': computers})
    context = {'computers': Computers.objects.all().order_by('name') }
    return render(request, 'computers/index.html', context)

def get_computers_by_highest(request):
    context = {'computers': Computers.objects.all().order_by('-price')}
    return render(request, 'computers/index.html', context)

def get_computers_by_lowest(request):
    context = {'computers': Computers.objects.all().order_by('price')}
    return render(request, 'computers/index.html', context)

def get_computers_by_name(request):
    context = {'computers': Computers.objects.all().order_by('name')}
    return render(request, 'computers/index.html', context)



def get_computers_by_id(request, id):
    return render(request, 'computers/computers_details.html', {
        'computers': get_object_or_404(Computers, pk=id)
    })


