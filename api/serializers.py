from rest_framework.serializers import ModelSerializer
from .models import Person, Expense, Settlement, House


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class SettlementSerializer(ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'


class HouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'