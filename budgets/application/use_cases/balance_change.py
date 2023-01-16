import decimal
from dataclasses import dataclass
from budgets.domain import value_objects
from budgets.infrastructure import models


class CreateBalanceChangeUseCase:
    @dataclass
    class Request:
        budget: int
        type: value_objects.BudgetBalanceChangeType
        amount: decimal.Decimal
        description: str
        owner: int

    def execute(self, request: Request) -> None:
        models.BudgetBalanceChange.objects.create(
            budget=request.budget,
            type=request.type.value,
            amount=request.amount,
            description=request.description,
            owner=request.owner
        )