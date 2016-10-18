from django.db import models


class Customers(models.Model):
    """
    Append to user registration
    """
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=18)
    regis_date = models.DateTimeField(auto_now_add=False, auto_now=True)  # Registration timestamp

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.username