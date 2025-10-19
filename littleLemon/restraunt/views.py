from django.shortcuts import render
from .models import MenuItem
from django.shortcuts import redirect, get_object_or_404

def home(request):
    return render(request, 'home.html')
def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True)
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)


def signup(request):
    return render(request, 'signup.html')