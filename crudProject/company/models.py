from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from PIL import Image

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=14)
    webPage = models.CharField(default="", max_length=250)
    email01 = models.EmailField(default="", max_length=254)
    email02 = models.EmailField(default="", max_length=254)
    logo = models.ImageField(
        default='company/default.png', upload_to='company/logo_pics')

    # Main Address
    line1 = models.CharField(max_length=200, default="")
    line2 = models.CharField(max_length=200, default="")
    zipCode = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        super().save(force_insert, force_update,
                     using, update_fields)

        img = Image.open(self.logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.logo.path)


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
