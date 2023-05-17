from django import forms
from .models import UserFile
from django.forms import ModelForm 
class UserForm(ModelForm):
    class Meta:
        model=UserFile
        fields={
            'file',
        }
