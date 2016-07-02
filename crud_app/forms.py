__author__ = 'shahjalal'
from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'street',
            'house_no',
            'postal_code',
            'town',
            'country',
            'newsletter',
        )
