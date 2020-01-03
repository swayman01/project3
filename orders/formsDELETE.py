import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

print("forms.py 6: Can we delete EditSaladForm?")

# Commented out 12/23/19
# classTopping.Form(forms.Form):
#     class Meta:
#         model = Authork
#         fields = '__all__'


# Commented out 12/23/19
# class EditSaladForm(forms.Form):
#     #TODO Add Data Verification
#     name = forms.CharField(label="Name")
#     price = forms.DecimalField(max_digits=5, decimal_places=2,label="Price")
#     #TODO: Add Validations
    # TODO Figure out what this means
    # def clean_renewal_date(self):
    #     data = self.cleaned_data['name']
        #return data
# class PlaceOrderForm(forms.Form):
#     place_order = forms.CharField(max_length=100, initial="orderJSONdata", \
#     help_text="orderJSONdata")
#     testfield = forms.CharField(label="testfield", max_length=100, initial="orderJSONdata", \
#     help_text="orderJSONdata")
#
#     def clean_place_order(self):
#         data = self.cleaned_data['place_order']
#         return data

# Commented out 12/19/19
# data = {'place_order':'23: place_order test'}
# f = PlaceOrderForm(data)
# # print("25 f.is_valid(): ", f.is_valid())
# # print("26 cleaned_data: ", f.cleaned_data)
# # print("27 PlaceOrderForm(data): ",f)
# class NameForm(forms.Form):
#     practice2 = forms.CharField(max_length=100, help_text="orderdataJSON goes here", initial ="practice2")

# from https://realpython.com/django-and-ajax-form-submissions/
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         # exclude = ['author', 'updated', 'created', ]
#         fields = ['text']
#         widgets = {
#             'text': forms.TextInput(attrs={
#                 'id': 'post-text',
#                 'required': True,
#                 'placeholder': 'Say something...'
#             }),
#         }
