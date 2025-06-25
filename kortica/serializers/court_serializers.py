from ..models import Court
from rest_framework import serializers
from kortica.serializers import ClubSerializer



class CourtSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)

    class Meta:
        model = Court
        fields = '__all__'
