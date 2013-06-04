from cms.plugin_base import CMSPluginBase
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from djangocms_wymeditor_plugin.models import HTMLText
from djangocms_wymeditor_plugin.forms import WYMeditorForm
from djangocms_wymeditor_plugin.utils import plugin_tags_to_user_html

class WYMeditorPlugin(CMSPluginBase):
    model = HTMLText
    form = WYMeditorForm
    render_template = "wymeditor_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'body': plugin_tags_to_user_html(instance.body, context,
                                             placeholder),
            'placeholder': placeholder,
            'object': instance
            })
        return context

plugin_pool.register_plugin(WYMeditorPlugin)
