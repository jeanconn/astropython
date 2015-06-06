"""
Contains forms that we shall use in a particular app
"""
from django import forms
from .models import CodeSnippet, Tutorial
from django.contrib.admin.widgets import AdminDateWidget
from astropython.settings import INPUT_CHOICES

M = CodeSnippet
class CustomForm(forms.ModelForm):
    class Meta:
        global M
        model = M
        fields = '__all__'
        widgets ={
            'categories':forms.CheckboxSelectMultiple()
        }
    def __init__(self,**kwargs):
        M = kwargs.pop('model')
        print M
        super(CustomForm, self).__init__(**kwargs)