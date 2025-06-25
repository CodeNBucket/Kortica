from ..models import Reservation
from rest_framework import serializers

from kortica.serializers.payment_serializers import PlayerPaymentSerializer 
from ..models import PlayerPayment
class ReservationSerializer(serializers.ModelSerializer):
    payments = PlayerPaymentSerializer(source='playerpayment_set', many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id', 'court', 'date', 'start_time', 'end_time',
            'total_price', 'player_no', 'created_by', 'payments'
        ]

    def create(self, validated_data):
        user = validated_data['created_by']
        total_price = validated_data['total_price']
        player_no = validated_data['player_no']

        reservation = Reservation.objects.create(**validated_data)

        PlayerPayment.objects.create(
            reservation=reservation,
            user=user,
            amount_paid=total_price / player_no,
            paid=False
        )

        return reservation
