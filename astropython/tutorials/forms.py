"""
Contains forms that we shall use in a particular app
"""
from django import forms
from .models import CodeSnippet

from django_ace import AceWidget # To add ACE code editor

class TypeForm(forms.Form):
    pass

class CodeModelForm(forms.ModelForm):
    body = forms.CharField(widget=AceWidget(mode='css', theme='twilight')) #adding the ACE code editor
    class Meta:
        model=CodeSnippet #Model that the form belongs to
        fields="__all__"