import datetime
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from user.models import Profile

from games.models import Games
# Create your views here
def index(request):
    return render(request, 'cart/index.html')

#def get_user_pending_order(request, **kwargs):
 #   user_profile = get_object_or_404(Profile, user=request.user)
  #  order = Order.objects.filter(owner=user_profile, is_ordered=False)
  #  if order.exists():
 #       return order[0]
  #  return 0

#def add_to_cart(request, **kwargs):
#    user_profile = get_object_or_404(Profile, user=request.user)
 #   games = Games.objects.filter(id=kwargs.get('item_id', "")).first()
 #   order_item, status = OrderItem.objects.get_or_create(games=games)
 #   user_order, status = Order.objects.get_or_create(owner=user_profile,is_ordered=False)
 #   user_order.items.add(order_item)
  #  if status:
 #       user_order


