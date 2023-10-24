from django.urls import path
from .views import expense_views, person_views, settlement_views

urlpatterns = [
    path('add-expense/', expense_views.add_expense, name='add_expense'),
    path('add-person/', person_views.add_person, name='add_person'),
    path('add-settlement/', settlement_views.add_settlement, name='add_settlement'),
]
