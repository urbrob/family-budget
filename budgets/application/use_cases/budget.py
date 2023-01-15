from dataclasses import dataclass

from budgets.infrastructure import models


class CreateBudgetUseCase:
    @dataclass
    class Request:
        name: str
        user_id: int

    def execute(self, request: Request) -> None:
        models.Budget.objects.create(name=request.name, owner_id=request.user_id)


class DeleteBudgetUseCase:
    @dataclass
    class Request:
        budget_id: int
        user_id: int

    def execute(self, request: Request) -> None:
        models.Budget.objects.filter(
            id=request.budget_id, owner_id=request.user_id
        ).delete()


class UpdateBudgetUseCase:
    @dataclass
    class Request:
        budget_id: int
        name: str

    def execute(self, request: Request) -> None:
        models.Budget.objects.filter(id=request.budget_id).update(name=request.name)
