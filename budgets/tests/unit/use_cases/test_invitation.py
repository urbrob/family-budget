from budgets.application import use_cases
from budgets.infrastructure import models
from budgets.tests import utils, factories


class CreateInvitationUseCaseTestCase(utils.BaseTest):
    def test_should_create_invitation_for_user(self):

        # Given
        second_user = factories.UserFactory()
        budget = factories.BudgetFactory(owner=self.user)
        request = use_cases.SendInvitationUseCase.Request(
            budget_id=budget.id, user_id=second_user.id
        )
        # When
        use_cases.SendInvitationUseCase().execute(request)

        # Then
        self.assertModelExist(
            models.BudgetMembership,
            budget_id=budget.id,
            user_id=second_user.id,
            accepted=False,
        )


class AcceptInvitationUseCaseTestCase(utils.BaseTest):
    def test_should_create_invitation_for_user(self):

        # Given
        budget = factories.BudgetFactory(owner=self.user)
        invitation = factories.BudgetMembershipFactory(user=self.user, budget=budget)
        request = use_cases.AcceptInvitationUseCase.Request(invitation_id=invitation.id)
        # When
        use_cases.AcceptInvitationUseCase().execute(request)

        # Then
        self.assertModelExist(
            models.BudgetMembership,
            budget_id=budget.id,
            user_id=self.user.id,
            accepted=True,
        )
