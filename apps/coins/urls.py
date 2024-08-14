from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GeekCoinViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'coins', GeekCoinViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


