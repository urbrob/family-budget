from dataclasses import dataclass

from budgets.infrastructure import models


class SendInvitationUseCase:
    @dataclass
    class Request:
        budget_id: int
        user_id: int

    def execute(self, request: Request) -> None:
        models.BudgetMembership.objects.create(
            budget_id=request.budget_id, user_id=request.user_id
        )


class AcceptInvitationUseCase:
    @dataclass
    class Request:
        invitation_id: int

    def execute(self, request: Request) -> None:
        models.BudgetMembership.objects.filter(id=request.invitation_id).update(
            accepted=True
        )
