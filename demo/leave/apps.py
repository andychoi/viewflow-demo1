from django.apps import AppConfig
from material.frontend.apps import ModuleMixin
from django.utils.translation import gettext_lazy as _


class LeaveConfig(AppConfig,ModuleMixin):
    name = 'demo.leave'
    icon = '<i class="material-icons">backup</i>'
    verbose_name = _("Leave")


