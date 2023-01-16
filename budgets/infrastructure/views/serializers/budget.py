from rest_framework import serializers
from django.db.models import Sum

from budgets.application.policies import budget as budget_polcies
from budgets.infrastructure.views.serializers import balance_change
from budgets.infrastructure import models
from budgets.infrastructure.views.serializers import utils


class CreateBudgetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = models.Budget
        fields = ("name",)


class BudgetSerializer(serializers.ModelSerializer):
    balance_changes = balance_change.BalanceChangeSerializer(read_only=True, many=True)

    def to_representation(self, instance: models.Budget) -> dict:
        data = super().to_representation(instance)
        data["balance"] = (
            models.BudgetBalanceChange.objects.filter(budget=data["id"])
            .aggregate(Sum("amount"))
            .get("amount__sum", 0)
        )
        return data

    class Meta:
        model = models.Budget
        fields = ("name", "id", "balance_changes")


class UpdateBudgetSerializer(utils.ModelWithPolicySerializer):
    policies = [budget_polcies.budget_belongs_to_user_policy]
    id = serializers.IntegerField(required=True)
    owner_id = serializers.IntegerField(required=True)

    class Meta:
        model = models.Budget
        fields = ("name", "id", "owner_id")


class DeleteBudgetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = models.Budget
        fields = ("id",)
