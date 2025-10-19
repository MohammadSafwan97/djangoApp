from django.shortcuts import render
from .models import MenuItem
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.db import transaction

def home(request):
    return render(request, 'home.html')
def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True)
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)


def signup(request):
    return render(request, 'signup.html')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()
        email = request.POST.get('email').strip()
        phone = request.POST.get('phone').strip()
        address = request.POST.get('address').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Basic validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')

        with transaction.atomic():
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            # Profile is automatically created via signal, now update phone & address
            user.profile.phone = phone
            user.profile.address = address
            user.profile.save()

        login(request, user)  # Log the user in immediately
        return redirect('home')  # Redirect to homepage after signup

    return render(request, 'signup.html')
