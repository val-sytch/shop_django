from django.test import TestCase
from django.utils import timezone
from djog.models.model_dogs import Breeds, Dogs

# Create your tests here.


class DogsModelTest(TestCase):
"""
Create dog item
"""
    def craeate_Dogs(self, breeds="Mutantdog", description="Very angry", price="2500", age="120", quantity="1.5",
                       alias="Home helper"):
        return Dogs.objects.craeate(breeds=breeds, description=description, price=price, age=age,
                                      quantity=quantity, timestamp=timezone.now())
"""
Breeds class test 
"""
    def test_breed_creation(self):
        breed = Breeds(breed="Mutantdog")
        self.assertEqual(str(breed), breed.breed)

"""
Breeds meta class test
"""
	def test_verbose_name_plural(self):
    	self.assertEqual(str(Entry._meta.verbose_name_plural), "Breeds")

