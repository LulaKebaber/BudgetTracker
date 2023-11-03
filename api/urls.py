from django.urls import path
from .views import expense_views, person_views, settlement_views, house_views

urlpatterns = [
    path('add-expense/', expense_views.add_expense, name='add_expense'), # прокинул
    path('add-person/', person_views.add_person, name='add_person'), # прокинул
    path('add-settlement/', settlement_views.add_settlement, name='add_settlement'), # прокинул
    path('get-debt/<str:telegram_id>/', settlement_views.get_debt, name='get_debt'),
    path('create-house/', house_views.create_house, name='create_house'), # прокинул
    path('add-house-member/', house_views.add_house_member, name='add_house_member'), # прокинул
    path('get-house-info/<str:house_name>/', house_views.get_house_info, name='get_house_info') # прокинул
]
