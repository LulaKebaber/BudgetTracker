from django.test import TestCase
from ..models import Person, House, Expense, Settlement


class UserTestCase(TestCase):

    def setUp(self):
        self.user = Person.objects.create(username='kebaber', telegram_id='123')

    def test_user_can_be_created(self):
        self.assertEqual(self.user.username, 'kebaber')
        self.assertEqual(self.user.telegram_id, '123')