from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from ..models import Person
from ..serializers import person_serializer


@swagger_auto_schema(method='post', request_body=person_serializer.AddPersonSerializer)
@api_view(['POST'])
def add_person(request):
    if 'person_name' in request.data and 'telegram_id' in request.data:
        person_name = request.data['person_name']
        telegram_id = request.data['telegram_id']
    else:
        return Response({'message': 'Invalid request'}, status=400)

    if Person.objects.filter(telegram_id=telegram_id).exists():
        return Response({'message': 'Person already exists!'}, status=400)

    person = Person.objects.create(person_name=person_name, telegram_id=telegram_id)
    return Response({'message': 'Person added!'}, status=201)