from django.db import models
from cms.models import CMSPlugin
from django.utils.text import Truncator

class HTMLText(CMSPlugin):
    body = models.TextField("body")
    search_fields = (body,)

    def __unicode__(self):
        return u'%s' % Truncator(strip_tags(self.body)[:30]).words(3)
