from dataclasses import dataclass

from budgets.application import exceptions
from budgets.infrastructure import models


class CreateBudgetUseCase:
    @dataclass
    class Request:
        name: str
        user_id: int

    def execute(self, request: Request) -> None:
        models.Budget.objects.create(name=request.name, owner_id=request.user_id)