"""
Contains forms that we shall use in a particular app
"""
from django import forms
from .models import CodeSnippet, Tutorial
from django.contrib.admin.widgets import AdminDateWidget
from astropython.settings import INPUT_CHOICES

from django_ace import AceWidget # To add ACE code editor
from tinymce.widgets import TinyMCE
from epiced.widgets import EpicEditorWidget

class HeaderForm(forms.Form):
    title = forms.CharField(max_length=200)#Title of the Post
    input_type= forms.ChoiceField(widget=forms.RadioSelect, choices=INPUT_CHOICES)
    abstract = forms.CharField(widget=forms.Textarea) #Short abstract of the tutorial

class WYSIWYGTutorialBody(forms.Form):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 50}))

class MarkdownTutorialBody(forms.Form):
    body= forms.CharField(widget=EpicEditorWidget())

class WYSIWYGCodeBody(WYSIWYGTutorialBody):
    snippet = forms.CharField(widget=AceWidget(mode='css', theme='twilight')) #adding the ACE code editor

class MarkdownCodeBody(MarkdownTutorialBody):
    snippet = forms.CharField(widget=AceWidget(mode='css', theme='twilight')) #adding the ACE code editor

class WYSIWYGSeriesTutorialBody(WYSIWYGTutorialBody):
    order_no= forms.IntegerField(min_value=1)

class MarkdownSeriesTutorialBody(MarkdownTutorialBody):
    order_no= forms.IntegerField(min_value=1)

class ResourceBody(forms.Form):
    start_date = forms.CharField(widget=AdminDateWidget)#Date the course starts#FIX THIS
    instructor_names = forms.CharField(max_length=400)#Names of Instructors
    website = forms.URLField()#Website hosting the course, or having more info about the course
    background = forms.CharField(widget=forms.Textarea)#Recommended Backgroud
    language = forms.CharField(max_length=200)#Language in which course is to be conducted

class WYSIWYGResourceBody(WYSIWYGTutorialBody,ResourceBody):
    syllabus = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 30})) #Syllabus or contents of the course
    faq=forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 30}))#FAQ if any

class MarkdownResourceBody(MarkdownTutorialBody,ResourceBody):
    syllabus = forms.CharField(widget=EpicEditorWidget()) #Syllabus or contents of the course
    faq=forms.CharField(widget=EpicEditorWidget())#FAQ if any

class TailForm(forms.ModelForm):
    class Meta:
        model =Tutorial
        fields=['categories','tags']
        widgets ={
            'categories':forms.CheckboxSelectMultiple()
        }

class SeriesForm(forms.Form):
    title = forms.CharField(max_length=200)#Title of the Post
    abstract = forms.CharField(widget=forms.Textarea) #Short abstract of the tutorial