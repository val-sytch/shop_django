from django.contrib import admin
from djog.models.model_dogs import Breeds, Dogs
from djog.models.model_customers import Customers
from djog.models.model_orders import Orders

class DogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'alias', 'breed', 'price', 'created', 'updated')

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'second_name', 'email', 'password', 'regis_date')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('item', 'customer', 'name', 'surname','phone', 'email', 'created' )

admin.site.register(Breeds)
admin.site.register(Dogs, DogsAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Orders, OrdersAdmin)