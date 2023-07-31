from rest_framework import serializers
from .models import MotivationQuote

class MotivationQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivationQuote
        fields = '__all__'
