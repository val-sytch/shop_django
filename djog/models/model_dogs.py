from django.db import models


class Breeds(models.Model):
    """
    Category
    """
    breed = models.CharField(max_length=120, verbose_name='Breed name')
    alias = models.SlugField(verbose_name='Breed alias')

    class Meta:
        verbose_name = "Breed"
        verbose_name_plural = "Breeds"

    def __str__(self):
        return self.breed


class Dogs(models.Model):
    """
    Main class
    
    """
    alias = models.SlugField(verbose_name='Item alias')
    breed = models.ForeignKey(Breeds)
    description = models.TextField(max_length=1000, verbose_name='Short description')
    image = models.CharField(max_length=100, verbose_name='Image URL')
    price = models.IntegerField(default=0, verbose_name='Price')
    age = models.IntegerField(default=0, verbose_name='Age')
    availability = models.BooleanField(default=True, verbose_name='Availability')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Dog"
        verbose_name_plural = "Dogs"

    def __str__(self):
        return str(self.id)
