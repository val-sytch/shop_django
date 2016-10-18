from django.db import models
from djog.models.model_dogs import Dogs
from djog.models.model_customers import Customers

class Orders(models.Model):
    """
    The fields of the orders
    """
    CREATED = 1
    IN_PROGRESS = 2
    WAITING_FOR_PAYMENT = 3
    WAITING_FOR_SHIPPED = 4
    WAITING_FOR_ARRIVED = 5
    ARRIVED = 6
    CLOSED = 7
    STATUS_CHOICES = (
        (CREATED, 'Created'),
        (IN_PROGRESS, 'In Progress'),
        (WAITING_FOR_PAYMENT, 'Waiting for payment'),
        (WAITING_FOR_SHIPPED, 'Waiting for shipped'),
        (WAITING_FOR_ARRIVED, 'Waiting for arrived'),
        (ARRIVED, 'Arrived'),
        (CLOSED, 'Closed'),
        )

    customer = models.ForeignKey(Customers, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=CREATED)
    name = models.CharField(max_length=10, verbose_name='Name')
    surname = models.CharField(max_length=10, verbose_name='Surname')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    email = models.EmailField(max_length=20, null=True, verbose_name='E-mail')
    item = models.ForeignKey(Dogs)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.id)
