"""
Contains forms that we shall use in a particular app
"""
from django import forms
from .models import CodeSnippet,Tutorial
from astropython.settings import INPUT_CHOICES

from django_ace import AceWidget # To add ACE code editor
from tinymce.widgets import TinyMCE
from epiced.widgets import EpicEditorWidget

TYPE_CHOICES = (
	('Single Tutorial', 'Single Tutorial'),
	('Tutorial Series', 'Tutorial Series'),
    ('Code Snippet','Code Snippet'),
    ('Educational Resource','Educational Resource'),
 )

class InputTypeForm(forms.Form):
    type_choice=forms.ChoiceField(choices=TYPE_CHOICES,widget=forms.RadioSelect())
    input_choice=forms.ChoiceField(choices=INPUT_CHOICES,widget=forms.RadioSelect())

class TitleForm(forms.ModelForm):
    class Meta:
        model=Tutorial
        fields = ['title','abstract']

class BodyFormWYSIWYG(forms.ModelForm):
    class Meta:
        model=Tutorial
        fields = ['body']
        widgets = {
            'body':TinyMCE(attrs={'cols': 200, 'rows': 100}),
            }

class BodyFormMarkdown(forms.ModelForm):
    class Meta:
        model=Tutorial
        fields = ['body']
        widgets = {
            'body':EpicEditorWidget(),
            }

class CategorizeForm(forms.ModelForm):
    class Meta:
        model=Tutorial
        fields = ['categories','tags']


class CodeModelForm(forms.ModelForm):
    body = forms.CharField(widget=AceWidget(mode='css', theme='twilight')) #adding the ACE code editor
    class Meta:
        model=CodeSnippet #Model that the form belongs to
        fields="__all__"