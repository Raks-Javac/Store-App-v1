from rest_framework.routers import DefaultRouter
from .views import VerifyPaymentViewSet, GetReferencePaymentViewSet

router = DefaultRouter()
router.register('get-payment', GetReferencePaymentViewSet, basename='payment-get')

router.register('verify-payment', VerifyPaymentViewSet, basename='payment-verification')

urlpatterns = router.urls