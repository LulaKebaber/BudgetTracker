from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import Person, House


class HouseAPITestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        self.person = Person.objects.create(username='test_owner', telegram_id='123')
        self.house = House.objects.create(house_name='test_house', owner=self.person)

    def test_create_house(self):
        data = {
            'house_name': 'new_test_house',
            'owner': self.person.telegram_id
        }
        url = reverse('create_house')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'House created!')
        self.assertEqual(House.objects.get(house_name='new_test_house').owner, self.person)
        self.assertEqual(House.objects.filter(house_name='new_test_house').count(), 1)

    def test_add_house_member(self):
        member = Person.objects.create(username='test_member', telegram_id='456')
        data = {
            'house_name': self.house.house_name,
            'username': member.username,
            'owner': self.person.telegram_id  # owner of the house
        }
        url = reverse('add_house_member')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Member added!')
        self.assertEqual(
            House.objects.get(house_name=self.house.house_name)
            .members.filter(username='test_member')
            .count(),
            1
        )
        self.assertEqual(self.house.members.filter(username='test_member').count(), 1)

    def test_get_house_info(self):
        url = reverse('get_house_info', args=[self.house.house_name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['house_name'], 'test_house')
        self.assertEqual(response.data['owner'], 'test_owner')

    def test_get_house_info_not_exist(self):
        url = reverse('get_house_info', args=["nonexistent_house"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ExpenseAPITestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        self.person = Person.objects.create(username='test_owner', telegram_id='123')
        self.house = House.objects.create(house_name='test_house', owner=self.person)

    def test_add_expense(self):
        data = {
            'amount': 100,
            'description': 'test_expense',
            'buyer': self.person.telegram_id,
            'date': '2021-01-01',
            'house_name': self.house.house_name
        }
        url = reverse('add_expense')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Expense added!')


class PersonAPITestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls'))
    ]

    def setUp(self):
        self.person = Person.objects.create(username='test_owner', telegram_id='123')
        self.house = House.objects.create(house_name='test_house', owner=self.person)

    def test_add_person(self):
        data = {
            'username': 'test_member',
            'telegram_id': '789'
        }
        url = reverse('add_person')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Person added!')
        self.assertEqual(Person.objects.filter(username='test_member').count(), 1)


class SettlementAPITestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls'))
    ]

    def setUp(self):
        self.person = Person.objects.create(username='test_owner', telegram_id='123')
        self.house = House.objects.create(house_name='test_house', owner=self.person)
        self.member = Person.objects.create(username='test_member', telegram_id='456')
        self.house.members.add(self.member)
        self.house.members.add(self.person)

    def test_add_settlement(self):
        data = {
            'amount': 100,
            'payer': self.person.telegram_id,
            'username': self.member.username,
        }
        url = reverse('add_settlement')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Settlement added!')

    def test_get_debt(self):
        url = reverse('get_debt', args=[self.person.telegram_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
