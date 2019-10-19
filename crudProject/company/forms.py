from django import forms
from .models import Company, CompanyAddress


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country']


class CompanyAddressForm(forms.ModelForm):
    class Meta:
        model = CompanyAddress
        fields = ['addressType', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country']
