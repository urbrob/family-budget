from rest_framework import serializers

from budgets.application.policies import balance_change as balance_change_policy
from budgets.infrastructure import models
from budgets.infrastructure.views.serializers import utils


class BalanceChangeSerializer(utils.ModelWithPolicySerializer):
    policies = [balance_change_policy.user_has_access_to_budget]
    class Meta:
        model = models.BudgetBalanceChange
        fields = ("budget", "type", "amount", "description", "owner")



