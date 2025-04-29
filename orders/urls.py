from django.urls import path, include
from rest_framework_nested import routers
from .views import OrderViewSet
from  rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('order', OrderViewSet, basename='orders')

urlpatterns = router.urls