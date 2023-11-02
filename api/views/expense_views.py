from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from ..models import Person, Expense
from ..serializers import expense_serializer


@swagger_auto_schema(method='post', request_body=expense_serializer.AddExpenseSerializer)
@api_view(['POST'])
def add_expense(request):
    if 'amount' in request.data and 'description' in request.data and 'date' in request.data and 'buyer' in request.data:
        amount = request.data['amount']
        description = request.data['description']
        date = request.data['date']
        buyer = request.data['buyer']

        try:
            buyer = Person.objects.get(telegram_id=buyer)
        except Person.DoesNotExist:
            return Response({'message': 'Buyer not found'}, status=400)

        expense = Expense.objects.create(amount=amount, description=description, date=date, buyer=buyer)
        return Response({'message': 'Expense added!'}, status=201)
    else:
        return Response({'message': 'Invalid request'}, status=400)