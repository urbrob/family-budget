from django import test
from budgets.tests import factories

class ApiTestCase(test.TestCase):
    def setUp(self) -> None:
        self.user = factories.UserFactory()
        self.client = test.Client()
        self.authenticated_client = test.Client()
        self.authenticated_client.login(username=self.user.username, password="12345")