from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Kleber Soares',
            cpf='12345678901',
            email='kleberss@gmail.com',
            phone='99-999999999'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have on auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
