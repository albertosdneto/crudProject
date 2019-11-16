"""Forms for company app."""

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.layout import Field
from django import forms
from .models import Company, CompanyAddress


class CustomImageField(Field):
    """A custom field to send image."""

    template = 'company/custom_imagefield.html'


class CompanyForm(forms.ModelForm):
    """A form to save company data."""

    cnpj = forms.CharField(label='Tax ID Number',
                           widget=forms.TextInput(attrs={'size': '15'}))

    line1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Street and Number'})
    )
    line2 = forms.CharField(
        label='Apartment, floor, etc.',
        widget=forms.TextInput(
            attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    email01 = forms.EmailField(
        label='Email for Public Relations',
        widget=forms.TextInput(
            attrs={'placehoolder': 'Email for PR'})

    )
    email02 = forms.EmailField(
        label='Email for Support',
        widget=forms.TextInput(
            attrs={'placehoolder': 'Email for Support'})

    )
    webPage = forms.CharField(
        label='Web Page',
        widget=forms.TextInput(
            attrs={'placeholder': 'Web Page'})
    )

    class Meta:
        """Model and fields that compose the form."""

        model = Company
        fields = ('name', 'cnpj', 'email01', 'email02', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country',
                  'webPage', 'logo')

    def __init__(self, *args, **kwargs):
        """Change form presentation."""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('cnpj', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email01', css_class='form-group col-md-6 mb-0'),
                Column('email02', css_class='form-group col-md-6 mb-0'),
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
            Row(
                Column('webPage', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            CustomImageField('logo'),
            Submit('submit', 'Submit')
        )


class CompanyFormUpdate(forms.ModelForm):
    """A form to update company details."""

    class Meta:
        """Fields that compose the form."""

        model = Company
        fields = '__all__'


class CompanyAddressForm(forms.ModelForm):
    """Form to save and update an address."""

    class Meta:
        """Form model and fields."""

        model = CompanyAddress
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Change form presentation at initialization."""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'companyAddressForm'
        self.helper.layout = Layout(
            Row(
                Column('company', css_class='form-group col-md-6 mb-0'),
                Column('addressType', css_class='form-group col-md-6 mb-0'),
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
            Submit('submit', 'Submit')
        )
