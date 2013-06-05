from django.conf import settings
from django.forms import CharField

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from djangocms_wymeditor_plugin.models import HTMLText
from djangocms_wymeditor_plugin.widget import WYMeditorWidget
from djangocms_wymeditor_plugin.forms import WYMeditorForm
from djangocms_wymeditor_plugin.utils import plugin_tags_to_user_html

class WYMeditorPlugin(CMSPluginBase):
    model = HTMLText
    form = WYMeditorForm
    render_template = "wymeditor_plugin.html"

    def get_editor_widget(self, request, plugins):
        return WYMeditorWidget(installed_plugins=plugins)

    def get_form_class(self, request, plugins):
        class WYMPluginForm(self.form):
            pass
        widget = self.get_editor_widget(request, plugins)
        WYMPluginForm.declared_fields["body"] = CharField(widget=widget,
                                                          required=False)
        return WYMPluginForm

    def get_form(self, request, obj=None, **kwargs):
        plugins = plugin_pool.get_text_enabled_plugins(
            self.placeholder,
            self.page
        )

        form = self.get_form_class(request, plugins)
        kwargs['form'] = form
        return super(WYMeditorPlugin, self).get_form(request, obj, **kwargs)
        
    def render(self, context, instance, placeholder):
        context.update({
            'body': plugin_tags_to_user_html(instance.body, context,
                                             placeholder),
            'placeholder': placeholder,
            'object': instance
            })
        return context

    def save_model(self, request, obj, form, change):
        obj.clean_plugins()
        super(WYMeditorPlugin, self).save_model(request, obj, form, change)

plugin_pool.register_plugin(WYMeditorPlugin)
