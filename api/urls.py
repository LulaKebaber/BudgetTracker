from django.urls import path
from .views import expense_views, person_views, settlement_views, house_views

urlpatterns = [
    path('add-expense/', expense_views.add_expense, name='add_expense'),
    path('add-person/', person_views.add_person, name='add_person'),
    path('add-settlement/', settlement_views.add_settlement, name='add_settlement'),
    path('get-debt/<str:telegram_id>/', settlement_views.get_debt, name='get_debt'),
    path('get-all-persons/', person_views.get_all_persons, name='get_all_persons'),
    path('create-house/', house_views.create_house, name='create_house'),
    path('add-house-member/', house_views.add_house_member, name='add_house_member'),
    path('get-house-info/', house_views.get_house_info, name='get_house_info')
]
