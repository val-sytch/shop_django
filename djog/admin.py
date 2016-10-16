from django.contrib import admin
from djog.models.models import Breeds, Dogs
from djog.user.models import SingUp

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('breeds', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'breeds')


admin.site.register(Dogs, ItemAdmin)
admin.site.register(Breeds, CategoryAdmin)
