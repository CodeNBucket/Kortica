from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClubViewSet, CourtViewSet, ReservationViewSet, PlayerPaymentViewSet
from kortica.views.user_views import RegisterAPIView,LogoutView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'courts', CourtViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'player-payments', PlayerPaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterAPIView.as_view(), name='register'),
    path('logout/',LogoutView.as_view(),name='logout') # needs refresh token as post request

]
