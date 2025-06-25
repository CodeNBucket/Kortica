from rest_framework import viewsets
from ..models import PlayerPayment
from kortica.serializers import PlayerPaymentSerializer


class PlayerPaymentViewSet(viewsets.ModelViewSet):
    queryset = PlayerPayment.objects.all()
    serializer_class = PlayerPaymentSerializer
