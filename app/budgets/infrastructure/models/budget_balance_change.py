from django.db import models
from django.contrib.auth import get_user_model

from budgets.domain import value_objects
from budgets.infrastructure.models import mixins, Budget

User = get_user_model()


class BudgetBalanceChange(mixins.CreateAndUpdateMixin, models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='balance_changes')
    description = models.CharField(max_length=256)
    type = models.CharField(
        max_length=8,
        choices=value_objects.BudgetBalanceChangeType.choices()
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance_changes')
