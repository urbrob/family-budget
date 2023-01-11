from django.apps import AppConfig
from importlib import import_module

from django.utils.module_loading import module_has_submodule

MODELS_MODULE_NAME = 'infrastructure.models.__init__'


class BudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'budgets'

    def import_models(self) -> None:
        self.models = self.apps.all_models[self.label]

        if module_has_submodule(self.module, MODELS_MODULE_NAME):
            models_module_name = "%s.%s" % (self.name, MODELS_MODULE_NAME)
            self.models_module = import_module(models_module_name)
