# Create your tests here.
from django import urls

from budgets.tests.integration.views import utils
from budgets.infrastructure import models

class RegisterViewTests(utils.ApiTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.payload = {
            'username': 'name',
            'password': 'pass1234!@#$',
            'email': 'name@name.pl'
        }
    def test_user_can_register(self) -> None:
        # Given
        # When
        response = self.client.post(urls.reverse('register'), self.payload)
        # Then
        self.assertEqual(response.status_code, 201)
        self.assertModelExist(models.User, username=self.payload['username'], email=self.payload['email'])

    def test_user_can_not_register_with_this_same_username(self) -> None:
        # Given
        self.payload['username'] = self.user.username
        # When
        response = self.client.post(urls.reverse('register'), self.payload)
        # Then
        self.assertEqual(response.status_code, 400)
        self.assertModelNotExist(models.User, username=self.payload['username'], email=self.payload['email'])