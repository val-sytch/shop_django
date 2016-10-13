from django.db import models
import datetime
#Create your models here

class Breeds(models.Model):
    """Category"""
    breed = models.CharField(max_length=120, verbose_name='Breed name')
    alias = models.SlugField(verbose_name='Breed alias')

    class Meta:
        verbose_name = "Breed"
        verbose_name_plural = "Breeds"

    def __str__(self):
        return 'Breed %s' % self.breed


class Dogs(models.Model):
    """Dagz, do ya like dagz?"""
    breeds = models.ForeignKey(Breeds)
    description = models.TextField(max_length=1000, verbose_name="Short description")
    image = models.CharField(max_length=100, verbose_name='Image URL')
    price = models.IntegerField(default=0, verbose_name='Price')
    age = models.IntegerField(default=0, verbose_name="Age")
    quantity = models.IntegerField(default=0, verbose_name='Quantity')
    alias = models.SlugField(verbose_name='Item alias')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return 'Breed %s' % self.breeds