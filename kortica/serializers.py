from rest_framework import serializers
from .models import User, Club, Court, Reservation, PlayerPayment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'phone_number', 'tennis_level', 'padel_level',
                  'profile_photo', 'is_manager','date_joined']

class ClubSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Club
        fields = '__all__'

class CourtSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)

    class Meta:
        model = Court
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    court = CourtSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'

class PlayerPaymentSerializer(serializers.ModelSerializer):
    player = UserSerializer(read_only=True)
    reservation = ReservationSerializer(read_only=True)

    class Meta:
        model = PlayerPayment
        fields = '__all__'
