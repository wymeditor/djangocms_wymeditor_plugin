import json

from django.conf import settings
from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation.trans_real import get_language

from djangocms_wymeditor_plugin import settings as text_settings
class WYMeditorWidget(Textarea):
    class Media:
        js = ('%sjquery.js' % settings.STATIC_URL,
              '%sjquery.wymeditor.min.js' % settings.STATIC_URL)

    def __init__(self, installed_plugins=None, attrs=None):
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMeditorWidget, self).__init__(self.attrs)
        self.installed_plugins = installed_plugins

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]
        context = {
            'name': name,
            'language': language,
            'STATIC_URL': settings.STATIC_URL,
            'WYM_TOOLS': mark_safe(text_settings.WYM_TOOLS),
            'WYM_CONTAINERS': mark_safe(text_settings.WYM_CONTAINERS),
            'WYM_CLASSES': mark_safe(text_settings.WYM_CLASSES),
            'WYM_STYLES': mark_safe(text_settings.WYM_STYLES),
            'WYM_STYLESHEET': mark_safe(text_settings.WYM_STYLESHEET),
            'installed_plugins': self.installed_plugins,
        }
        return mark_safe(render_to_string('wymeditor.html', context))

    def render(self, name, value, attrs=None):
        return super(WYMeditorWidget, self).render(name, value, attrs) + \
           self.render_additions(name, value, attrs)
