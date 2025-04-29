from django.urls import path, include
from rest_framework_nested import routers
from . import views
from cart.views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register('list', views.CartViewSet, basename='list')

carts_router = routers.NestedDefaultRouter(router, 'list', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + carts_router.urls
