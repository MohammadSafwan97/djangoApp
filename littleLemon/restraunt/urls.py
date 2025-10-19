from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='Menu'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]

