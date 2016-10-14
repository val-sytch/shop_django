from django.contrib import admin
from djog.models.model_dogs import Breeds, Dogs
from djog.models.model_user_registration import SingUp

admin.site.register(Breeds)
admin.site.register(Dogs)
admin.site.register(SingUp)
