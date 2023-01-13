from django.db import models as django_models
from django.contrib.auth import get_user_model
from budgets.domain import value_objects
from budgets.infrastructure import models
from budgets.infrastructure.models import mixins

User = get_user_model()


class BudgetBalanceChange(mixins.CreateAndUpdateMixin, django_models.Model):
    amount = django_models.DecimalField(max_digits=8, decimal_places=2)
    budget = django_models.ForeignKey(
        models.Budget, on_delete=django_models.CASCADE, related_name="balance_changes"
    )
    description = django_models.CharField(max_length=256)
    type = django_models.CharField(
        max_length=8, choices=value_objects.BudgetBalanceChangeType.choices()
    )
    owner = django_models.ForeignKey(
        User, on_delete=django_models.CASCADE, related_name="balance_changes"
    )
