from django import forms
from .models import Company, CompanyAddress
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
# from crispy_forms.layout import Layout, Field, Div, MultiField, Submit
# from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.layout import Field


class CustomImageField(Field):
    template = 'company/custom_imagefield.html'
# class Row(Div):
#     css_class = "form-row"


class CompanyForm(forms.ModelForm):
    cnpj = forms.CharField(label='Tax ID Number',
                           widget=forms.TextInput(attrs={'size': '15'}))

    line1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Street and Number'})
    )
    line2 = forms.CharField(
        label=' ',
        widget=forms.TextInput(
            attrs={'placeholder': 'Apartment, studio, or floor'})
    )

    class Meta:
        model = Company
        fields = ('name', 'cnpj', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country', 'logo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'companyForm'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('cnpj', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('line1', css_class='form-group col-md-6 mb-0'),
                Column('line2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('zipCode', css_class='form-group col-md-2 mb-0'),
                Column('city', css_class='form-group col-md-2 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('country', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            CustomImageField('logo'),  # <-- Here
            Submit('submit', 'Register')
        )


class CompanyAddressForm(forms.ModelForm):
    class Meta:
        model = CompanyAddress
        fields = ['addressType', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country']
