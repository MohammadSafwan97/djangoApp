from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MenuItemViewSet, BookingViewSet

# --- API Routers ---
router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # --- HTML Views ---
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('signup/', views.signup, name='signup'),

    # --- API Endpoints ---
    path('api/', include(router.urls)),
]
