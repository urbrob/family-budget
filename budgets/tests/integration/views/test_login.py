# Create your tests here.
from django import urls

from budgets.tests.integration.views import utils

class LoginTests(utils.ApiTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.payload = {
            "username": self.user.username,
            "password": 'pass'
        }

    def test_login_return_access_and_refresh_tokens(self) -> None:
        # Given

        # When
        response = self.client.post(urls.reverse('login'), self.payload)
        # Then
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_can_login_when_in_database_with_correct_password(self) -> None:
        # Given

        # When
        response = self.client.post(urls.reverse('login'), self.payload)
        # Then
        self.assertEqual(response.status_code, 200)

    def test_user_can_not_login_with_incorrect_password(self) -> None:
        # Given
        self.payload['password'] = 'NOT_A_PASSWORD'
        # When
        response = self.client.post(urls.reverse('login'), self.payload)
        # Then
        self.assertEqual(response.status_code, 401)


    def test_user_can_not_login_with_not_existing_account(self) -> None:
        # Given
        self.payload['username'] = 'IDONOTEXIST'
        # When
        response = self.client.post(urls.reverse('login'), self.payload)
        # Then
        self.assertEqual(response.status_code, 401)