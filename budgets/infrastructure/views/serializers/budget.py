from rest_framework import serializers

from budgets.infrastructure import models


class CreateBudgetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = models.Budget
        fields = ("name",)


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = ("name", "id")


class DeleteBudgetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    class Meta:
        model = models.Budget
        fields = ("id",)

