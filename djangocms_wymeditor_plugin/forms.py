from django import forms
from django.forms.models import ModelForm
from djangocms_wymeditor_plugin.models import HTMLText
from djangocms_wymeditor_plugin.widget import WYMeditorWidget

class WYMeditorForm(ModelForm):
    text = forms.CharField(label="", widget=WYMeditorWidget())
    
    class Meta:
        model = HTMLText
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type'
        )

    def __init__(self, wym_customizations=None, *args, **kwargs):
        super(WYMeditorForm, self).__init__(*args, **kwargs)
        if wym_customizations:
            self.fields['text'] = forms.CharField(label="",
                    widget=WYMeditorWidget(customizations=wym_customizations))
