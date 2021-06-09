from django.db import models


class Address(models.Model):
    number = models.IntegerField('Numero')
    street = models.CharField('Rua', max_length=200)
    district = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=100)

    def __str__(self):
        return f"{self.number} - {self.street} - {self.district} -\
            {self.city} - {self.state}"


class Sellers(models.Model):
    name = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('EMAIL', max_length=60)
    phone = models.CharField('Telefone', max_length=20)
    address = models.OneToOneField(
        Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
