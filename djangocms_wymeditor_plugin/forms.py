from django import forms
from djangocms_wymeditor_plugin.widget import WYMeditorWidget

class WYMeditorForm(forms.Form):
    text = forms.CharField(label="", widget=WYMeditorWidget())

    def __init__(self, wym_customizations=None, *args, **kwargs):
        super(WYMeditorForm, self).__init__(*args, **kwargs)
        if wym_customizations:
            self.fields['text'] = forms.CharField(label="",
                    widget=WYMeditorWidget(customizations=wym_customizations))
