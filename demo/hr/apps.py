from django.apps import AppConfig
from material.frontend.apps import ModuleMixin
from material.frontend.registry import modules


class HrConfig(AppConfig,ModuleMixin):
    name = 'demo.hr'
    label = 'hr'
    verbose_name='Human Resource Management'
    icon = '<i class="material-icons">book</i>'
