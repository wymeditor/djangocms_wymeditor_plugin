from django import forms
from django.forms.models import ModelForm

from djangocms_wymeditor_plugin.models import HTMLText


class WYMeditorForm(ModelForm):
    body = forms.CharField()

    class Meta:
        model = HTMLText
        exclude = ('page', 'position', 'placeholder',
                   'language', 'plugin_type')
