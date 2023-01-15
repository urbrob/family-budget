# Create your tests here.
from django import urls

from budgets.tests.integration.views import utils
from budgets.tests import factories
from budgets.infrastructure import models


class BudgetViewTests(utils.ApiTestCase):
    def setUp(self) -> None:
        super().setUp()
        factories.BudgetFactory.create_batch(15, owner=self.user)

    def test_user_can_create_budget(self) -> None:
        # Given
        budget_name = "House"
        # When
        response = self.authenticated_client.post(
            urls.reverse("budget"), {"name": budget_name}
        )
        # Then
        self.assertEqual(response.status_code, 201)
        self.assertModelExist(models.Budget, name=budget_name, owner_id=self.user.id)

    def test_user_can_not_create_budget_with_empty_name(self) -> None:
        # Given
        budget_name = ""
        # When
        response = self.authenticated_client.post(
            urls.reverse("budget"), {"name": budget_name}
        )
        # Then
        self.assertEqual(response.status_code, 400)
        self.assertModelNotExist(models.Budget, name=budget_name, owner_id=self.user.id)

    def test_user_can_not_create_budget_without_log_in(self) -> None:
        # Given
        budget_name = "House"
        # When
        response = self.client.post(urls.reverse("budget"), {"name": budget_name})
        # Then
        self.assertEqual(response.status_code, 401)

    def test_user_can_return_all_his_budgets(self) -> None:
        # Given

        # When
        response = self.authenticated_client.get(urls.reverse("budget"))
        response_body = response.data
        # Then

        self.assertEqual(
            len(response_body["results"]),
            models.Budget.objects.filter(owner=self.user).count(),
        )

    def test_user_can_return_all_his_budgets_with_pagination(self) -> None:
        # Given
        limit = 5
        offset = 5
        # When
        response = self.authenticated_client.get(
            urls.reverse("budget"), data={"limit": limit, "offset": offset}
        )
        response_body = response.data
        # Then

        self.assertEqual(len(response_body["results"]), limit)

    def test_user_can_return_all_his_budgets_with_name_filter(self) -> None:
        # Given
        sepecial_budget = factories.BudgetFactory(name="special", owner=self.user)

        # When
        response = self.authenticated_client.get(
            urls.reverse("budget"), data={"name": sepecial_budget.name}
        )
        response_body = response.data["results"]
        # Then

        self.assertEqual(len(response_body), 1)
        self.assertEqual(response_body[0]["name"], sepecial_budget.name)

    def test_user_can_not_get_budgets_when_he_is_not_authenticated(self) -> None:
        # Given

        # When
        response = self.client.get(urls.reverse("budget"))
        # Then
        self.assertEqual(response.status_code, 401)

    def test_user_can_delete_his_budget(self) -> None:
        # Given
        sepecial_budget = factories.BudgetFactory(name="special", owner=self.user)

        # When
        response = self.authenticated_client.delete(
            urls.reverse("budget"), {"id": sepecial_budget.id}
        )
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertModelNotExist(models.Budget, id=sepecial_budget.id)

    def test_user_can_not_delete_someone_else_budget(self) -> None:
        # Given
        special_user = factories.UserFactory()
        sepecial_budget = factories.BudgetFactory(name="special", owner=special_user)

        # When
        response = self.authenticated_client.delete(
            urls.reverse("budget"), {"id": sepecial_budget.id}
        )
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertModelExist(models.Budget, id=sepecial_budget.id)

    def test_user_can_not_delete_budgets_when_he_is_not_authenticated(self) -> None:
        # Given

        # When
        response = self.client.delete(urls.reverse("budget"), {"id": 1})
        # Then
        self.assertEqual(response.status_code, 401)

    def test_user_can_update_his_budget(self) -> None:
        # Given
        special_budget = factories.BudgetFactory(name="special", owner=self.user)
        new_name = "VERY special budget"

        # When
        response = self.authenticated_client.put(
            urls.reverse("budget"), {"name": new_name, "id": special_budget.id}
        )
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertModelExist(models.Budget, name=new_name)

    def test_user_can_not_update_someone_else_budget(self) -> None:
        # Given
        special_user = factories.UserFactory()
        special_budget = factories.BudgetFactory(name="special", owner=special_user)
        new_name = "VERY special budget"

        # When
        response = self.authenticated_client.put(
            urls.reverse("budget"), {"name": new_name, "id": special_budget.id}
        )
        # Then
        self.assertEqual(response.status_code, 400)
        self.assertModelNotExist(models.Budget, name=new_name)

    def test_user_can_not_delete_budgets_when_he_is_not_authenticated(self) -> None:
        # Given

        # When
        response = self.client.put(
            urls.reverse("budget"), {"name": "Special name", "id": 1}
        )
        # Then
        self.assertEqual(response.status_code, 401)
