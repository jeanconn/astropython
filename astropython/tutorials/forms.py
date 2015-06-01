"""
Contains forms that we shall use in a particular app
"""
from django import forms
from .models import CodeSnippet, Tutorial
from astropython.settings import INPUT_CHOICES

from django_ace import AceWidget # To add ACE code editor
from tinymce.widgets import TinyMCE
from epiced.widgets import EpicEditorWidget

class HeaderForm(forms.Form):
    title = forms.CharField(max_length=200)#Title of the Post
    input_type= forms.ChoiceField(widget=forms.RadioSelect, choices=INPUT_CHOICES)
    abstract = forms.CharField(widget=forms.Textarea) #Short abstract of the tutorial

class WYSIWYGBodyForm(forms.Form):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 50}))

class MarkdownBodyForm(forms.Form):
    body= forms.CharField(widget=EpicEditorWidget())

class TailForm(forms.Form):
    class Meta:
        models=Tutorial
        fields=['categories','tags']

class CodeModelForm(forms.ModelForm):
    body = forms.CharField(widget=AceWidget(mode='css', theme='twilight')) #adding the ACE code editor
    class Meta:
        model=CodeSnippet #Model that the form belongs to
        fields="__all__"