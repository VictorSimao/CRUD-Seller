from django.contrib import admin
from .models import Sellers


class sellersAdmin(admin.ModelAdmin):
     class Meta:
        model = Sellers
        fields = ['name', 'cpf', 'email', 'phone']


admin.site.register(Sellers)
