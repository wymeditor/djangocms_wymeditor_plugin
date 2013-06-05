from django.db import models
from cms.models import CMSPlugin
from django.utils.text import Truncator
from django.utils.html import strip_tags
from djangocms_wymeditor_plugin.utils import plugin_tags_to_id_list, clean_html

class HTMLText(CMSPlugin):
    body = models.TextField("body")

    search_fields = ('body',)

    def __unicode__(self):
        return u'%s' % Truncator(strip_tags(self.body)[:30]).words(3)

    def clean(self):
        self.body = clean_html(self.body, full=False)
    
    def clean_plugins(self):
        ids = plugin_tags_to_id_list(self.body)
        plugins = CMSPlugin.objects.filter(parent=self)
        for plugin in plugins:
            if not plugin.pk in ids:
                plugin.delete()
