# Create your tests here.
from django import urls

from budgets.tests.integration.views import utils
from budgets.tests import factories
from budgets.domain import value_objects
from budgets.infrastructure import models


class BalanceChangeViewTests(utils.ApiTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.budget = factories.BudgetFactory.create(owner=self.user)


    def test_user_can_create_balance_change(self) -> None:
        # Given
        payload = {
            "budget": self.budget.id,
            "type": value_objects.BudgetBalanceChangeType.INCOME.value,
            "amount": "100",
            "description": "Very much moni",
        }
        # When
        response = self.authenticated_client.post(
            urls.reverse("balance_change"), payload
        )
        # Then
        self.assertEqual(response.status_code, 201)
        self.assertModelExist(models.BudgetBalanceChange, **payload)