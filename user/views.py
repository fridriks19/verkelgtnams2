from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from user.forms.profile_form import ProfileForm
from user.models import Profile
from cart.models import Order


def register(request):
    if request.method =='POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    user_orders = Order.objects.filter(is_ordered=True, owner=profile)
    context = {
        'user_orders': user_orders
    }

    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', context, {
        'form': ProfileForm(instance=profile)
    })
