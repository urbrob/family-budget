# Create your tests here.
from django import urls

from budgets.tests.integration.views import utils
from budgets.tests import factories
from budgets.infrastructure import models

class CreateBudgetViewTests(utils.ApiTestCase):
    def setUp(self) -> None:
        super().setUp()
        factories.BudgetFactory.create_batch(15, owner=self.user)


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
        budget_name = 'House'
        # When
        response = self.client.post(urls.reverse('budget'), {'name': budget_name})
        # Then
        self.assertEqual(response.status_code, 401)

    def test_user_can_return_all_his_budgets(self) -> None:
        # Given

        # When
        response = self.authenticated_client.get(urls.reverse('budget'))
        response_body = response.data
        # Then

        self.assertEqual(len(response_body['results']), models.Budget.objects.filter(owner=self.user).count())

    def test_user_can_return_all_his_budgets_with_pagination(self) -> None:
        # Given

        # When
        response = self.authenticated_client.get(urls.reverse('budget'), data={'limit': 5, 'offset': 5})
        response_body = response.data
        # Then

        self.assertEqual(len(response_body['results']), 5)

    def test_user_can_not_get_budgets_when_he_is_not_authenticated(self) -> None:
        # Given

        # When
        response = self.client.get(urls.reverse('budget'))
        # Then
        self.assertEqual(response.status_code, 401)