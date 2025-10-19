from django.shortcuts import render
from .models import MenuItem
from django.shortcuts import redirect, get_object_or_404

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')



def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True)
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)

def add_to_cart(request, item_id):
    # Example: simple session-based cart
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('menu')  # redirect back to menu page