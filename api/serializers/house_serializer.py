from rest_framework.serializers import ModelSerializer
from ..models import House


class CreateHouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class AddPersonToHouseSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class GetHouseInfoSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = ['house_name', 'members', 'owner']