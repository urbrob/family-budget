from django import urls
from budgets.tests import utils
from rest_framework import test


class ApiTestCase(utils.BaseTest):
    def setUp(self) -> None:
        super().setUp()
        self.client = test.APIClient()
        token = self.client.post(urls.reverse('login'), {'username': self.user.username, 'password': 'pass'}).data['access']
        self.authenticated_client = test.APIClient()
        self.authenticated_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')