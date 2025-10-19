# restraunt/urls.py
from django.urls import path
from restraunt import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('signup/', views.signup, name='signup'),
]
