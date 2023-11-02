from rest_framework.serializers import ModelSerializer
from ..models import Settlement


class AddSettlementSerializer(ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'