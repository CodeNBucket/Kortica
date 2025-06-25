from ..models import Club
from rest_framework import serializers
from kortica.serializers import UserSerializer

class ClubSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Club
        fields = '__all__'