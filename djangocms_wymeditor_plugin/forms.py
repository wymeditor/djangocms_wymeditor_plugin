from django import forms
from django.forms.models import ModelForm
from djangocms_wymeditor_plugin.models import HTMLText
from djangocms_wymeditor_plugin.widget import WYMeditorWidget

class WYMeditorForm(ModelForm):
    body = forms.CharField()
    
    class Meta:
        model = HTMLText
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type'
        )
