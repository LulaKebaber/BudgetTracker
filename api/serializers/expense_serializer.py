from rest_framework.serializers import ModelSerializer
from ..models import Expense


class AddExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'