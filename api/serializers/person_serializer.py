from rest_framework.serializers import ModelSerializer
from ..models import Person


class AddPersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class GetPersonsSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'