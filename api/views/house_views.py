from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from ..serializers import house_serializer
from ..models import House, Person


@swagger_auto_schema(method='post', request_body=house_serializer.CreateHouseSerializer)
@api_view(['POST'])
def create_house(request):
    if 'house_name' in request.data and 'owner' in request.data:
        house_name = request.data['house_name']
        owner = request.data['owner']
    else:
        return Response({'message': 'Invalid request'}, status=400)

    if not Person.objects.get(telegram_id=owner):
        return Response({'message': 'Owner is required'}, status=400)

    if House.objects.filter(house_name=house_name).exists():
        return Response({'message': 'House already exists!'}, status=400)

    owner = Person.objects.get(telegram_id=owner)
    house = House.objects.create(house_name=house_name, owner=owner)
    house.members.add(owner)

    return Response({'message': 'House created!'}, status=201)


@swagger_auto_schema(method='post', request_body=house_serializer.AddPersonToHouseSerializer)
@api_view(['POST'])
def add_house_member(request):
    if 'house_name' in request.data and 'username' in request.data and 'owner' in request.data:
        house_name = request.data['house_name']
        username = request.data['username']
        owner = request.data['owner']
    else:
        return Response({'message': 'Invalid request'}, status=400)

    if not Person.objects.filter(username=username).exists():
        return Response({'message': 'Member does not exist!'}, status=400)

    if not Person.objects.filter(telegram_id=owner).exists():
        return Response({'message': 'Owner does not exist!'}, status=400)

    if not House.objects.filter(house_name=house_name).exists():
        return Response({'message': 'House does not exist!'}, status=400)

    if int(House.objects.get(house_name=house_name).owner.telegram_id) != owner:
        return Response({'message': 'You have no access to this house!'}, status=400)

    house = House.objects.get(house_name=house_name)
    person = Person.objects.get(username=username)

    house.members.add(person)
    return Response({'message': 'Member added!'}, status=201)


@swagger_auto_schema(method='get')
@api_view(['GET'])
def get_house_info(request, house_name):
    if not House.objects.filter(house_name=house_name).exists():
        return Response({'message': 'House does not exist!'}, status=400)

    house = House.objects.get(house_name=house_name)
    members = list(house.members.values('username', 'telegram_id'))

    return Response({
        'house_name': house.house_name,
        'owner': house.owner.username,
        'members': members
    }, status=200)
