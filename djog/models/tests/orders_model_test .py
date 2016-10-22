from django.test import TestCase
from django.utils import timezone
from djog.models.model_orders import Orders
from djog.models.model_dogs import Dogs
from djog.models.model_customers import Customers


class OrdersModelTest(TestCase):
    def craeate_Orders(self, status="4", name="Killa", surname="Dous", phone="45458645", email="testcase@exaple.com"):
    	"""
    	Creates fake(test) order
    	
    	"""

        return Orders.objects.craeate(name=name, surname=surname, phone=phone, email=email,
            craeated=timezone.now())

    def test_verbose_name_plural(self):
        """
         Name plural test

        """
        self.assertEqual(str(Orders._meta.verbose_name_plural), "Orders")