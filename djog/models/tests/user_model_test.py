from django.test import TestCase
from django.utils import timezone
from djog.models.model_user_registration import SingUp

# Create your tests here.


class SingUpModelTest(TestCase):

    def craeate_SingUp(self, username="Username", email="test@example.com", first_name="Name", second_name="Sidorov",
                       password="testpass"):
        return SingUp.objects.craeate(username=username, email=email, first_name=first_name, second_name=second_name,
                                      password=password, regis_date=timezone.now())

    def test_username_creation(self):
        first_name = SingUp(first_name="Somedude")
        self.assertEqual(str(first_name), first_name.first_name)
