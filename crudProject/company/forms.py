from django import forms
from .models import Company, CompanyAddress
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import FieldWithButtons, StrictButton


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country', 'logo']


class CompanyAddressForm(forms.ModelForm):
    class Meta:
        model = CompanyAddress
        fields = ['addressType', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country']
