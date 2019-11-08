from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.layout import Field
from django import forms
from .models import Company, CompanyAddress


class CustomImageField(Field):
    template = 'company/custom_imagefield.html'


class CompanyForm(forms.ModelForm):
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
        model = Company
        fields = ('name', 'cnpj', 'email01', 'email02', 'line1',
                  'line2', 'zipCode', 'city', 'state', 'country', 'webPage', 'logo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_id = 'companyForm'
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
    class Meta:
        model = Company
        fields = '__all__'


# class CompanyFormUpdate(CompanyForm):
#     class Meta:
#         model = Company
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'companyFormUpdate'
#         self.helper.layout = Layout(
#             Row(
#                 Column('name', css_class='form-group col-md-6 mb-0'),
#                 Column('cnpj', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('email01', css_class='form-group col-md-6 mb-0'),
#                 Column('email02', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('line1', css_class='form-group col-md-6 mb-0'),
#                 Column('line2', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('zipCode', css_class='form-group col-md-2 mb-0'),
#                 Column('city', css_class='form-group col-md-2 mb-0'),
#                 Column('state', css_class='form-group col-md-4 mb-0'),
#                 Column('country', css_class='form-group col-md-4 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('webPage', css_class='form-group col-md-2 mb-0'),
#                 css_class='form-row'
#             ),

#             CustomImageField('logo'),
#             Submit('submit', 'Submit')
#         )


class CompanyAddressForm(forms.ModelForm):
    class Meta:
        model = CompanyAddress
        # fields = ['addressType', 'line1', 'line2',
        #           'zipCode', 'city', 'state', 'country']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
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


class CompanyAddressFormHelper(FormHelper):
    class Meta:
        model = CompanyAddress
        # fields = ['addressType', 'line1', 'line2',
        #           'zipCode', 'city', 'state', 'country']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyAddressFormHelper, self).__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.layout = Layout(
            Row(
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
        self.render_required_fields = True
