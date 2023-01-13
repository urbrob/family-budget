# Create your tests here.
from django import urls

from budgets.tests.integration.views import utils
from budgets.infrastructure import models

class CreateBudgetViewTests(utils.ApiTestCase):
    def test_user_can_create_budget(self) -> None:
        # Given
        budget_name = 'House'
        # When
        response = self.authenticated_client.post(urls.reverse('budget'), {'name': budget_name})
        # Then
        self.assertEqual(response.status_code, 201)
        self.assertModelExist(models.Budget, name=budget_name, owner_id=self.user.id)

    def test_user_can_not_create_budget_with_empty_name(self) -> None:
        # Given
        budget_name = ''
        # When
        response = self.authenticated_client.post(urls.reverse('budget'), {'name': budget_name})
        # Then
        self.assertEqual(response.status_code, 400)
        self.assertModelNotExist(models.Budget, name=budget_name, owner_id=self.user.id)


    def test_user_can_not_create_budget_without_log_in(self) -> None:
        # Given
        budget_name = budget_name = 'House'
        # When
        response = self.client.post(urls.reverse('budget'), {'name': budget_name})
        # Then
        self.assertEqual(response.status_code, 401)