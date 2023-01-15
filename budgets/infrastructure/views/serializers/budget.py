from rest_framework import serializers

from budgets.application.policies import budget as budget_polcies
from budgets.infrastructure import models
from budgets.infrastructure.views.serializers import utils


class CreateBudgetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = models.Budget
        fields = ("name",)


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = ("name", "id")


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
