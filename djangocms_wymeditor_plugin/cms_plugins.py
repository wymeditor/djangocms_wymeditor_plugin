from cms.plugin_base import CMSPluginBase
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from djangocms_wymeditor_plugin.forms import WYMeditorForm

class WYMeditorPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "wymeditor_plugin.html"

    def render(self, context, instance, placeholder):
        form = WYMeditorForm(settings.WYMEDITOR_SETTINGS)
        context.update({'wymeditor_form': form})
        return context

plugin_pool.register_plugin(WYMeditorPlugin)
