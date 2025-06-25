from ..models import PlayerPayment
from rest_framework import serializers
from kortica.serializers import UserSerializer


class PlayerPaymentSerializer(serializers.ModelSerializer):
    player = UserSerializer(source='user', read_only=True)

    class Meta:
        model = PlayerPayment
        fields = ['id', 'player', 'amount_paid', 'paid']