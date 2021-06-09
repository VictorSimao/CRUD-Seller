from django.forms import ModelForm
from .models import Sellers, Address


class AddressForm(ModelForm):
      
      class Meta:
         model = Address
         fields = "__all__"

class sellersForm(ModelForm):
      
      class Meta:
         model = Sellers
         fields = ['name', 'cpf', 'email', 'phone']
