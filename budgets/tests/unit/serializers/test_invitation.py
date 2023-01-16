from budgets.tests import factories
from budgets.infrastructure.views import serializers
from budgets.tests.unit.serializers import utils


class SendInvitationSerializerTestCase(utils.SerializerTestCase):
    def test_validate_with_correct_data(self) -> None:
        # Given
        data = {"budget_id": 1, "email": "urb.rob@o2.pl", "owner_id": 2}
        # When
        serializer = serializers.SendInvitationSerializer(data=data, run_policies=False)
        # Then
        self.assertTrue(serializer.is_valid())

    def test_validate_with_missing_data_throw_errors(self) -> None:
        # Given
        data = {}
        expected_errors = {
            "email": ["This field is required."],
            "budget_id": ["This field is required."],
            "owner_id": ["This field is required."],
        }
        # When
        serializer = serializers.SendInvitationSerializer(data=data, run_policies=False)
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)


class AcceptInvitationSerializerTestCase(utils.SerializerTestCase):
    def test_validate_with_correct_data(self) -> None:
        # Given
        data = {"invitation_id": 1, "user_id": 1}
        # When
        serializer = serializers.AcceptInvitationSerializer(
            data=data, run_policies=False
        )
        # Then
        self.assertTrue(serializer.is_valid())

    def test_validate_with_missing_data_throw_errors(self) -> None:
        # Given
        data = {}
        expected_errors = {
            "invitation_id": ["This field is required."],
            "user_id": ["This field is required."],
        }
        # When
        serializer = serializers.AcceptInvitationSerializer(
            data=data, run_policies=False
        )
        serializer.is_valid()
        # Then
        self.assertValidationErrors(serializer, expected_errors)
