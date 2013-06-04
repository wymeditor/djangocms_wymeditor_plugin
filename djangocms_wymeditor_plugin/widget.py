from django.conf import settings
from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class WYMeditorWidget(Textarea):
    class Media:
        js = ('%sjquery.wymeditor.min.js' % settings.STATIC_URL,)

    def __init__(self, attrs=None, installed_plugins=None, pk=None):
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMeditorWidget, self).__init__(self.attrs)
        self.installed_plugins = installed_plugins
        self.pk = pk

    def render(self, name, value, attrs=None):
        additions = mark_safe(render_to_string('wymeditor.html'))
        return super(WYMeditorWidget, self).render(name, value, attrs) + \
            additions
