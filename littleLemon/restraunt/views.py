from django.shortcuts import render
from .models import MenuItem

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')



def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True)
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)
