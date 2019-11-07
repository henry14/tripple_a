from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField


class Pharmacy(models.Model):
    pharmacist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Drug(models.CharField):
    name = models.CharField(max_length=255)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=255)
    manufacture = models.DateField(verbose_name='Date of manufacture')
    expiry = models.DateField(verbose_name='Date of expiry')
    stocked_quantity = models.PositiveSmallIntegerField(verbose_name='Number of boxes stocked')
    cost = MoneyField(max_digits=19, decimal_places=4)

    @property
    def quantity_available(self):
        return None

    @property
    def quantity_sold(self):
        return None
