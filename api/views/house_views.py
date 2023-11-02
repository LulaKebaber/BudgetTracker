from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
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

    owner = Person.objects.get(telegram_id=owner)

    if not owner:
        return Response({'message': 'Owner is required'}, status=400)

    if House.objects.filter(house_name=house_name).exists():
        return Response({'message': 'House already exists!'}, status=400)

    house = House.objects.create(house_name=house_name, owner=owner)
    return Response({'message': 'House created!'}, status=201)


@swagger_auto_schema(method='post', request_body=house_serializer.AddPersonToHouseSerializer)
@api_view(['POST'])
def add_house_member(request):
    if 'house_name' in request.data and 'members' in request.data and 'owner' in request.data:
        house_name = request.data['house_name']
        members = request.data['members']
        owner = request.data['owner']
    else:
        return Response({'message': 'Invalid request'}, status=400)

    if not Person.objects.filter(telegram_id=members[0]).exists():
        return Response({'message': 'Member does not exist!'}, status=400)

    if not Person.objects.filter(telegram_id=owner).exists():
        return Response({'message': 'Owner does not exist!'}, status=400)

    if not House.objects.filter(house_name=house_name).exists():
        return Response({'message': 'House does not exist!'}, status=400)

    house = House.objects.get(house_name=house_name)
    house.members.add(members[0])
    return Response({'message': 'Member added!'}, status=201)


@swagger_auto_schema(method='get')
@api_view(['GET'])
def get_house_info(request, house_name):
    # if 'house_name' in request.data:
    #     house_name = request.data['house_name']
    # else:
    #     return Response({'message': 'Invalid request'}, status=400)

    if not House.objects.filter(house_name=house_name).exists():
        return Response({'message': 'House does not exist!'}, status=400)

    house = House.objects.get(house_name=house_name)

    return Response({
        'house_name': house.house_name,
        'owner': house.owner.person_name,
        'members': house.members
        # 'members': serializers.serialize("json", house.members)
    }, status=200)
