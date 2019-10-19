from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=14)

    # Main Address
    line1 = models.CharField(max_length=200, default="")
    line2 = models.CharField(max_length=200, default="")
    zipCode = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    # addresses = ArrayField(
    #     ArrayField(
    #         models.CharField(max_length=100, blank=True, null=True),
    #         size=9,
    #     ),
    #     blank=True,
    #     null=True,
    # )

    def __str__(self):
        return self.name


class CompanyAddress(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    addressType = models.CharField(max_length=50)
    line1 = models.CharField(max_length=200)  # Street or avenue, and number
    line2 = models.CharField(max_length=200)  # Additional Information
    zipCode = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.addressType
