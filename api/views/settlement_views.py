from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from ..models import Person, Settlement
from ..serializers import settlement_serializer

@swagger_auto_schema(method='post', request_body=settlement_serializer.AddSettlementSerializer)
@api_view(['POST'])
def add_settlement(request):
    if 'payer' in request.data and 'recipient' in request.data and 'amount' in request.data:
        payer = request.data['payer']
        recipient = request.data['recipient']
        amount = request.data['amount']

        try:
            payer = Person.objects.get(telegram_id=payer)
        except Person.DoesNotExist:
            return Response({'message': 'Payer not found'}, status=400)

        try:
            recipient = Person.objects.get(telegram_id=recipient)
        except Person.DoesNotExist:
            return Response({'message': 'Recipient not found'}, status=400)

        settlement = Settlement.objects.create(payer=payer, recipient=recipient, amount=amount)
        return Response({'message': 'Settlement added!'}, status=201)
    else:
        return Response({'message': 'Invalid request'}, status=400)
    

@swagger_auto_schema(method='get')
@api_view(['GET'])
def get_debt(request, telegram_id):
    try:
        person = Person.objects.get(telegram_id=telegram_id)
    except Person.DoesNotExist:
        return Response({'message': 'Person not found'}, status=404)

    debts = Settlement.objects.filter(payer=person)
    return Response([{
        'payer': debt.payer.telegram_id,
        'recipient': debt.recipient.telegram_id,
        'amount': debt.amount
    } for debt in debts])