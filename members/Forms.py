from django import forms
from django.forms import ModelForm
from .models import member


class member_form(ModelForm):
    class Meta:
        model=member
        fields='__all__'
        