import typing
from budgets.tests import utils
from rest_framework import serializers


class SerializerTestCase(utils.BaseTest):
    def assertValidationErrors(
        self,
        serializer: serializers.Serializer,
        expected_errors: typing.Dict[str, typing.List[str]],
    ) -> None:
        actual_errors = serializer.errors
        for field, expected_field_errors in expected_errors.items():
            field_occured_errors = actual_errors.get(field, [])
            self.assertTrue(
                set(expected_field_errors).issubset(set(field_occured_errors)),
                f'Missing errors for field "{field}". Expected errors: "{expected_field_errors}". Actual errors: "{field_occured_errors}"',
            )
