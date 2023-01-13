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
