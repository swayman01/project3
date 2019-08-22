import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
print("Can we delete forms.py?")
class EditSaladForm(forms.Form):
    #TODO Add Data Verification
    name = forms.CharField(label="Name")
    price = forms.DecimalField(max_digits=5, decimal_places=2,label="Price")
    #TODO: Add Validations
    # TODO Figure out what this means
    # def clean_renewal_date(self):
    #     data = self.cleaned_data['name']
        #return data
