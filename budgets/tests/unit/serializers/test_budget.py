from django import test
from budgets.infrastructure.views import serializers
from budgets.tests.unit.serializers import utils


class CreateBudgetSerializerTestCase(utils.SerializerTestCase):
    def test_validate_with_correct_data(self) -> None:
        # Given
        data = {
            'name': 'House',
        }
        # When
        serializer = serializers.CreateBudgetSerializer(data=data)
        # Then
        self.assertTrue(serializer.is_valid())

    def test_validate_with_missing_data_throw_errors(self) -> None:
        # Given
        data = {
        }
        expected_errors = {
            "name": ['This field is required.'],
        }
        # When
        serializer = serializers.CreateBudgetSerializer(data=data)
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)


