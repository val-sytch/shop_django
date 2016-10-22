from django.test import TestCase
from django.utils import timezone
from djog.models.model_dogs import Breeds, Dogs


class DogsModelTest(TestCase):
    """
    Item(dog) creation test

    """
    def craeate_dogs(self, alias="Home helper", breed="Mutantdog", description="Very angry",
                     price="2500", age="120", availability=False, quantity="1.5"):
        return Dogs.objects.craeate(alias=alias, breed=breed, description=description, price=price, age=age,
                                    quantity=quantity, availability=availability, craeated=timezone.now())

    def test_breed_creation(self):
        """
        Breed creation test

        """
        breed = Breeds(breed="Mutantdog")
        self.assertEqual(str(breed), breed.breed)

    def test_verbose_name_plural(self):
        """
         Name plural test

        """
        self.assertEqual(str(Breeds._meta.verbose_name_plural), "Breeds")
