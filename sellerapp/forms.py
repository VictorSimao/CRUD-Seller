from django.forms import ModelForm
from .models import Sellers


class sellersForm(ModelForm):
     class Meta:
        model = Sellers
        fields = ['name', 'cpf', 'email', 'phone']
