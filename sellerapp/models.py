from django.db import models


class Sellers(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=20)
