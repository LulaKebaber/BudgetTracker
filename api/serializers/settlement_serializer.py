from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Settlement


class AddSettlementSerializer(ModelSerializer):
    username = serializers.CharField(max_length=100)

    class Meta:
        model = Settlement
        fields = ['amount', 'payer', 'username']
