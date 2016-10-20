from django.test import TestCase
from django.utils import timezone
from djog.models.model_customers import Customers

class CustomersModelTest(TestCase):
    """
    Customers test

    """
    def craeate_Customer(self, username="Username", email="test@example.com", first_name="Name", second_name="Sidorov",
                       password="testpass"):
        return Customers.objects.craeate(username=username, email=email, first_name=first_name, second_name=second_name,
                                      password=password, regis_date=timezone.now())

    def test_username_creation(self):
        first_name = Customers(first_name="Somedude")
        self.assertEqual(str(first_name), first_name.first_name)
