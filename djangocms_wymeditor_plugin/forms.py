from django import forms
from django_wymeditor.widget import WYMeditorWidget

class WYMeditorForm(forms.Form):
    text = forms.CharField(widget=WYMeditorWidget)
