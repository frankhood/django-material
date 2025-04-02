from django.apps import AppConfig

from material.frontend.apps import ModuleMixin
from django.utils.translation import gettext_lazy as _


class EmployeesConfig(ModuleMixin, AppConfig):
    name = 'demo.examples.employees'
    icon = '<i class="material-icons">people</i>'
    verbose_name = _('Employees')

    def has_perm(self, user):
        return user.is_superuser
