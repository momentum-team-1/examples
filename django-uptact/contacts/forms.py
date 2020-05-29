from django import forms
from .models import Contact, Address


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'company_name',
            'phone_number',
            'email',
            'birthday',
        ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'address_type',
            'line_1',
            'line_2',
            'city',
            'state',
            'zip_code',
        ]
