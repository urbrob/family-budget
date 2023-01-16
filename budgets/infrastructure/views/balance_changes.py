import decimal

from budgets.application import use_cases
from budgets.domain import value_objects
from budgets.infrastructure.views import serializers
from budgets.infrastructure import models
from rest_framework import permissions, views, status, pagination


class BalanceChangeView(views.APIView, pagination.LimitOffsetPagination):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: views.Request) -> views.Response:
        data = {
            "budget": request.data.get("budget"),
            "type": request.data.get("type"),
            "amount": request.data.get("amount"),
            "description": request.data.get("description"),
            "owner": request.user.id,
        }
        serializer = serializers.BalanceChangeSerializer(data=data)
        if serializer.is_valid():
            request = use_cases.CreateBalanceChangeUseCase.Request(
                budget=serializer.validated_data["budget"],
                type=value_objects.BudgetBalanceChangeType(serializer.validated_data["type"]),
                amount=decimal.Decimal(serializer.validated_data["amount"]),
                description=serializer.validated_data["description"],
                owner=serializer.validated_data["owner"]
            )
            use_cases.CreateBalanceChangeUseCase().execute(request)
            return views.Response({"status": "OK"}, status=status.HTTP_201_CREATED)
        return views.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)