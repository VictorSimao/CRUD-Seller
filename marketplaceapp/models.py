from django.db import models


class ConfigMarketplace(models.Model):
    apis = models.CharField(max_length=200)
    keys = models.CharField(max_length=200)
    endpoints = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.apis} - {self.keys} - {self.endpoints}"


class Marketplace(models.Model):
    name = models.CharField(max_length=70)
    config_marketplace = models.OneToOneField(
        ConfigMarketplace,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
