from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from ..models import Person, Settlement, House
from ..serializers import settlement_serializer


@swagger_auto_schema(method='post', request_body=settlement_serializer.AddSettlementSerializer)
@api_view(['POST'])
def add_settlement(request):
    if 'payer' in request.data and 'username' in request.data and 'amount' in request.data:
        payer = request.data['payer']
        username = request.data['username']
        amount = request.data['amount']
    else:
        return Response({'message': 'Invalid request'}, status=400)

    if not Person.objects.filter(telegram_id=payer).exists():
        return Response({'message': 'Payer does not exist!'}, status=400)

    if not Person.objects.filter(username=username).exists():
        return Response({'message': 'Recipient does not exist!'}, status=400)

    if not House.objects.filter(members__telegram_id=payer) and not House.objects.filter(owner__telegram_id=payer):
        return Response({'message': 'Payer does not belong to any house!'}, status=400)

    if not House.objects.filter(members__username=username) and not House.objects.filter(owner__username=username):
        return Response({'message': 'Recipient does not belong to any house!'}, status=400)

    payer = Person.objects.get(telegram_id=payer)
    recipient = Person.objects.get(username=username)

    settlement = Settlement.objects.create(payer=payer, recipient=recipient, amount=amount)
    return Response({'message': 'Settlement added!'}, status=201)


# in progress
@swagger_auto_schema(method='get')
@api_view(['GET'])
def get_debt(request, telegram_id):
    if not Person.objects.filter(telegram_id=telegram_id).exists():
        return Response({'message': 'Person does not exist!'}, status=400)

    person = Person.objects.get(telegram_id=telegram_id)

    if not House.objects.filter(members__username=person.username) and not House.objects.filter(
            owner__telegram_id=telegram_id):
        return Response({'message': 'Person does not belong to any house!'}, status=400)

    house = House.objects.get(members__username=person.username)
    house_members = list(house.members.values('username', 'telegram_id'))

    debts = {}
    for member in house_members:
        debts[member['username']] = 0

    for settlement in Settlement.objects.filter(payer=person):
        debts[settlement.recipient.username] -= settlement.amount

    for settlement in Settlement.objects.filter(recipient=person):
        debts[settlement.payer.username] += settlement.amount


    return Response({'debts': debts}, status=200)