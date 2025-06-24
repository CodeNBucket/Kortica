from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClubViewSet, CourtViewSet, ReservationViewSet, PlayerPaymentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'courts', CourtViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'player-payments', PlayerPaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
