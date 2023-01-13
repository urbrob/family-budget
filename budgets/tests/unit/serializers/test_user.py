from django import test
from budgets.infrastructure.views import serializers
from budgets.tests.unit.serializers import utils


class UserRegisterSerializerTestCase(utils.SerializerTestCase):
    def test_validate_with_correct_data(self) -> None:
        # Given
        data = {"email": "test@test.pl", "username": "user", "password": "test1234!@#$"}
        # When
        serializer = serializers.UserRegisterSerializer(data=data)
        # Then
        self.assertTrue(serializer.is_valid())

    def test_validate_with_missing_data_throw_errors(self) -> None:
        # Given
        data = {}
        expected_errors = {
            "password": ["This field is required."],
            "username": ["This field is required."],
            "email": ["This field is required."],
        }
        # When
        serializer = serializers.UserRegisterSerializer(data=data)
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)

    def test_validate_with_incorrect_email_thorw_errors(self) -> None:
        # Given
        data = {"email": "test.pl", "username": "user", "password": "test1234!@#$"}
        expected_errors = {
            "email": ["Enter a valid email address."],
        }
        # When
        serializer = serializers.UserRegisterSerializer(data=data)
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)
