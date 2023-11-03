from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import House


class CreateHouseSerializer(ModelSerializer):

    class Meta:
        model = House
        fields = '__all__'


class AddPersonToHouseSerializer(ModelSerializer):
    username = serializers.CharField(max_length=150)

    class Meta:
        model = House
        fields = ['username', 'house_name', 'owner']


class GetHouseInfoSerializer(ModelSerializer):
    class Meta:
        model = House
        fields = ['house_name', 'members', 'owner']
