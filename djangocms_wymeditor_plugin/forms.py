from django import forms
from djangocms_wymeditor_plugin.widget import WYMeditorWidget

class WYMeditorForm(forms.Form):
    text = forms.CharField(widget=WYMeditorWidget)
