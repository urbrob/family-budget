from budgets.tests import utils
from budgets.application import use_cases, exceptions
from budgets.infrastructure import models


class UserRegistrationUseCaseTestCase(utils.BaseTest):
    def test_should_create_user(self):
        # Given
        request = use_cases.RegisterUserUseCase.Request(
            username="new_user", password="new_password", email="new_email@email.com"
        )
        # When
        use_cases.RegisterUserUseCase().execute(request)

        # Then
        self.assertModelExist(
            models.User, username=request.username, email=request.email
        )

    def test_should_not_create_user_with_taken_email(self):
        # Given
        request = use_cases.RegisterUserUseCase.Request(
            username="new_user", password="new_password", email=self.user.email
        )
        # When
        self.assertRaises(
            exceptions.UserAlreadyExist,
            use_cases.RegisterUserUseCase().execute,
            request,
        )

        # Then
        self.assertModelNotExist(
            models.User, username=request.username, email=request.email
        )
