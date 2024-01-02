from django.urls import path, include
from rest_framework import routers

from .views import StockViewSet

# Create a router object
router = routers.DefaultRouter()

# Register the StockViewSet with the router
router.register('stocks', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
