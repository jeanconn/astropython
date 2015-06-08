"""
Contains forms that we shall use in a particular app
"""
from django import forms
from .models import CodeSnippet, Tutorial
from django.contrib.admin.widgets import AdminDateWidget
from astropython.settings import INPUT_CHOICES

def PostForm(model_type,exclude_fields,*args,**kwargs):
    class PostForm(forms.ModelForm):
        class Meta:
            model=model_type
            exclude=exclude_fields

        def __init__(self):
            super(PostForm, self).__init__(*args, **kwargs)

    return PostForm()