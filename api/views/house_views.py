from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import House


@api_view(['POST'])
def create_house(request):
    if 'name' in request.data:
        name = request.data['name']
        owner = request.data['owner']
    else:
        return Response({'message': 'Invalid request'}, status=400)
    
    if House.objects.filter(name=name).exists():
        return Response({'message': 'House already exists!'}, status=400)
    
    house = House.objects.create(name=name, owner=owner)
    return Response({'message': 'House created!'}, status=201)


@api_view(['POST'])
def add_house_member(request):
    if 'house_name' in request.data and 'member' in request.data:
        house_name = request.data['house_name']
        member = request.data['member']
    else:
        return Response({'message': 'Invalid request'}, status=400)
    
    if not House.objects.filter(name=house_name).exists():
        return Response({'message': 'House does not exist!'}, status=400)
    
    house = House.objects.get(name=house_name)
    house.members.add(member)
    return Response({'message': 'Member added!'}, status=201)


@api_view(['GET'])
def get_house_info(request):
    if 'house_name' in request.data:
        house_name = request.data['house_name']
    else:
        return Response({'message': 'Invalid request'}, status=400)
    
    if not House.objects.filter(name=house_name).exists():
        return Response({'message': 'House does not exist!'}, status=400)
    
    house = House.objects.get(name=house_name)

    return Response({
        'name': house.name,
        'owner': house.owner,
        'members': house.members
    }, status=200)