# tasks.py

from celery import shared_task
from ..models import Expense, Person


@shared_task
def process_expense(amount, description, date, buyer):
    buyer = Person.objects.get(telegram_id=buyer)
    expense = Expense.objects.create(amount=amount, description=description, date=date, buyer=buyer)
