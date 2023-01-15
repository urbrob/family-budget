from budgets.tests import utils
from budgets.application import use_cases, exceptions
from budgets.infrastructure import models
from budgets.tests import factories


class CreateBudgetUseCaseTestCase(utils.BaseTest):
    def test_should_create_budget(self):
        # Given
        request = use_cases.CreateBudgetUseCase.Request(
            name="House", user_id=self.user.id
        )
        # When
        use_cases.CreateBudgetUseCase().execute(request)

        # Then
        self.assertModelExist(
            models.Budget, name=request.name, owner_id=request.user_id
        )


class DeleteBudgetUseCaseTestCase(utils.BaseTest):
    def test_should_delete_budget(self):
        # Given
        budget = factories.BudgetFactory(owner=self.user)
        self.assertModelExist(
            models.Budget, id=budget.id, owner_id=budget.owner_id
        )
        request = use_cases.DeleteBudgetUseCase.Request(
            budget_id=budget.id, user_id=self.user.id
        )
        # When
        use_cases.DeleteBudgetUseCase().execute(request)

        # Then
        self.assertModelNotExist(
            models.Budget, id=budget.id, owner_id=budget.owner_id
        )
