from django.db import models


class SingUp(models.Model):
    """
    Append to user registration
    """
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=18)
    regis_date = models.DateTimeField(auto_now_add=False, auto_now=True)  # Registration timestamp

    def __str__(self):
        return self.first_name