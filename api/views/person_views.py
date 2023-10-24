from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Person


@api_view(['POST'])
def add_person(request):
    if 'name' in request.data and 'telegram_id' in request.data:
        name = request.data['name']
        telegram_id = request.data['telegram_id']

        person = Person.objects.create(name=name, telegram_id=telegram_id)
        return Response({'message': 'Person added!'}, status=201)
    else:
        return Response({'message': 'Invalid request'}, status=400)