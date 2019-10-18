from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=14)
    addresses = ArrayField(
        ArrayField(
            models.CharField(max_length=100, blank=True, null=True),
            size=9,
        ),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
