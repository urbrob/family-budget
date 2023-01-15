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
            urls.reverse("invitation"),
            {"budget_id": self.budget.id, "email": self.second_user.email},
        )
        # Then
        self.assertEqual(response.status_code, 201)
        self.assertModelExist(
            models.BudgetMembership,
            budget=self.budget.id,
            user=self.second_user.id,
            accepted=False,
        )

    def test_user_can_not_invite_to_not_his_budget(self) -> None:
        # Given
        special_user = factories.UserFactory()
        special_budget = factories.BudgetFactory(owner=special_user)
        # When
        response = self.authenticated_client.post(
            urls.reverse("invitation"),
            {"budget_id": special_budget.id, "email": self.second_user.email},
        )
        # Then
        self.assertEqual(response.status_code, 400)
        self.assertModelNotExist(
            models.BudgetMembership, budget=special_budget.id, user=special_user
        )

    def test_user_can_not_invite_unauthorized(self) -> None:
        # Given
        # When
        response = self.client.post(
            urls.reverse("invitation"),
            {"budget_id": self.budget.id, "email": self.second_user.email},
        )
        # Then
        self.assertEqual(response.status_code, 401)
        self.assertModelNotExist(
            models.BudgetMembership, budget=self.budget.id, user=self.second_user
        )

    def test_user_can_accept_his_invitation(self) -> None:
        # Given
        special_user = factories.UserFactory()
        special_budget = factories.BudgetFactory(owner=special_user)
        invitation = factories.BudgetMembershipFactory(
            user=self.user, budget=special_budget
        )
        self.assertModelExist(
            models.BudgetMembership,
            budget=special_budget,
            user=self.user.id,
            accepted=False,
        )
        # When
        response = self.authenticated_client.patch(
            urls.reverse("invitation"), {"invitation_id": invitation.id}
        )
        # Then
        self.assertEqual(response.status_code, 201)
        self.assertModelExist(
            models.BudgetMembership,
            budget=special_budget,
            user=self.user.id,
            accepted=True,
        )

    def test_user_can_not_accept_someone_else_invitation(self) -> None:
        # Given
        special_user = factories.UserFactory()
        special_budget = factories.BudgetFactory(owner=special_user)
        not_logged_in_user = factories.UserFactory()
        invitation = factories.BudgetMembershipFactory(
            user=not_logged_in_user, budget=special_budget
        )
        self.assertModelExist(
            models.BudgetMembership,
            budget=special_budget,
            user=not_logged_in_user.id,
            accepted=False,
        )

        # When
        response = self.authenticated_client.patch(
            urls.reverse("invitation"), {"invitation_id": invitation.id}
        )
        # Then
        self.assertEqual(response.status_code, 400)
        self.assertModelExist(
            models.BudgetMembership,
            budget=special_budget,
            user=not_logged_in_user.id,
            accepted=False,
        )
        self.assertModelNotExist(
            models.BudgetMembership,
            budget=special_budget,
            user=self.user.id,
            accepted=True,
        )

    def test_should_return_users_invitations(self):
        # Given
        special_user = factories.UserFactory()
        budgets = factories.BudgetFactory.create_batch(2, owner=special_user)
        invitation = factories.BudgetMembershipFactory(user=self.user, budget=budgets[0])
        second_invitation = factories.BudgetMembershipFactory(user=self.user, budget=budgets[0])

        # When
        response = self.authenticated_client.get(urls.reverse("invitation"))
        results = response.data["results"]
        first_result = results[0]

        # Then
        self.assertEqual(len(results), 2)
        self.assertEqual(first_result['name'], budgets[0].name)
        self.assertEqual(first_result['owner'], special_user.email)
        self.assertEqual(first_result['accepted'], invitation.accepted)

