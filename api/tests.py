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
