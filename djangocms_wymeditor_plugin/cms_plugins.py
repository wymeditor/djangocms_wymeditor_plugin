from cms.plugin_base import CMSPluginBase
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from djangocms_wymeditor_plugin.models import HTMLText
from djangocms_wymeditor_plugin.forms import WYMeditorForm

class WYMeditorPlugin(CMSPluginBase):
    model = HTMLText
    form = WYMeditorForm
    render_template = "wymeditor_plugin.html"

    #def get_form(self, request, obj=None, **kwargs):
        #form = WYMeditorForm(settings.WYMEDITOR_SETTINGS)
        #kwargs['form'] = form
        #return super(WYMeditorPlugin, self).get_form(request, obj, **kwargs)


    def render(self, context, instance, placeholder):
        context.update({'body': instance.body})
        return context

plugin_pool.register_plugin(WYMeditorPlugin)
