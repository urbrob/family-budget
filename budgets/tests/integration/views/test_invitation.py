from django import urls

from budgets.tests.integration.views import utils
from budgets.tests import factories
from budgets.infrastructure import models


class InvitationViewTests(utils.ApiTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.budget = factories.BudgetFactory(owner=self.user)
        self.second_user = factories.UserFactory()

    def test_user_can_invite_to_his_budget(self) -> None:
        # Given
        # When
        response = self.authenticated_client.post(
            urls.reverse("invitation"), {"budget_id": self.budget.id, 'email': self.second_user.email}
        )
        # Then
        self.assertEqual(response.status_code, 201)
        self.assertModelExist(models.BudgetMembership, budget=self.budget.id, user=self.second_user.id, accepted=False)

    def test_user_can_not_invite_to_not_his_budget(self) -> None:
        # Given
        special_user = factories.UserFactory()
        special_budget = factories.BudgetFactory(owner=special_user)
        # When
        response = self.authenticated_client.post(
            urls.reverse("invitation"), {"budget_id": special_budget.id, 'email': self.second_user.email}
        )
        # Then
        self.assertEqual(response.status_code, 400)
        self.assertModelNotExist(models.BudgetMembership, budget=special_budget.id, user=special_user)

    def test_user_can_not_invite_unauthorized(self) -> None:
        # Given
        # When
        response = self.client.post(
            urls.reverse("invitation"), {"budget_id": self.budget.id, 'email': self.second_user.email}
        )
        # Then
        self.assertEqual(response.status_code, 401)
        self.assertModelNotExist(models.BudgetMembership, budget=self.budget.id, user=self.second_user)
