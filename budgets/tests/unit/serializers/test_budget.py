from budgets.tests import factories
from budgets.infrastructure.views import serializers
from budgets.tests.unit.serializers import utils


class CreateBudgetSerializerTestCase(utils.SerializerTestCase):
    def test_validate_with_correct_data(self) -> None:
        # Given
        data = {
            "name": "House",
        }
        # When
        serializer = serializers.CreateBudgetSerializer(data=data)
        # Then
        self.assertTrue(serializer.is_valid())

    def test_validate_with_missing_data_throw_errors(self) -> None:
        # Given
        data = {}
        expected_errors = {
            "name": ["This field is required."],
        }
        # When
        serializer = serializers.CreateBudgetSerializer(data=data)
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)


class BudgetSerializerTestCase(utils.SerializerTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.budget = factories.BudgetFactory(owner=self.user)

    def test_deserialize_with_budget_model(self) -> None:
        # Given
        # When
        serializer = serializers.BudgetSerializer(self.budget)
        data = serializer.data
        # Then
        self.assertEqual(self.budget.name, data["name"])
        self.assertEqual(self.budget.id, data["id"])


class DeleteSerializerTestCase(utils.SerializerTestCase):
    def test_validate_with_correct_data(self) -> None:
        # Given
        data = {
            "id": 1,
        }
        # When
        serializer = serializers.DeleteBudgetSerializer(data=data)
        # Then
        self.assertTrue(serializer.is_valid())

    def test_validate_with_missing_data_throw_errors(self) -> None:
        # Given
        data = {}
        expected_errors = {
            "id": ["This field is required."],
        }
        # When
        serializer = serializers.DeleteBudgetSerializer(data=data)
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)


class UpdateSerializerTestCase(utils.SerializerTestCase):
    def test_validate_with_correct_data(self) -> None:
        # Given
        data = {"id": 1, "name": "Grocery", "owner_id": 1}
        # When
        serializer = serializers.UpdateBudgetSerializer(data=data, run_policies=False)
        # Then
        self.assertTrue(serializer.is_valid())

    def test_validate_with_missing_data_throw_errors(self) -> None:
        # Given
        data = {}
        expected_errors = {
            "id": ["This field is required."],
            "name": ["This field is required."],
            "owner_id": ["This field is required."],
        }
        # When
        serializer = serializers.UpdateBudgetSerializer(data=data)
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)
