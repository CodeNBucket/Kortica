from rest_framework import viewsets
from .models import User, Club, Court, Reservation, PlayerPayment
from .serializers import UserSerializer, ClubSerializer, CourtSerializer, ReservationSerializer, PlayerPaymentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PlayerPaymentViewSet(viewsets.ModelViewSet):
    queryset = PlayerPayment.objects.all()
    serializer_class = PlayerPaymentSerializer
