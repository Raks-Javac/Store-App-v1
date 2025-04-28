from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')
router2 = routers.DefaultRouter()
router2.register('products', views.ProductViewSet, basename='products')

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
products_router.register('images', views.ProductImageViewSet,
                         basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')





docs_url = [
     # Swagger UI endpoints
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')), 
]

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls + docs_url + router2.urls
