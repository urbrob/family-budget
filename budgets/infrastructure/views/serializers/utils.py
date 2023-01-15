from rest_framework import serializers, fields


class ModelWithPolicySerializer(serializers.ModelSerializer):
    policies = []

    def __init__(self, instance=None, data=fields.empty, run_policies=True, **kwargs):
        super().__init__(instance, data, **kwargs)
        self.run_policies = run_policies

    def prepare_data_to_policies(self, attrs: dict):
        return attrs

    def validate(self, attrs: dict) -> dict:
        attrs = super().validate(attrs)
        if self.run_policies:
            try:
                attrs = self.prepare_data_to_policies(attrs)
                self.validate_policies(attrs)
            except Exception as e:
                raise serializers.ValidationError(e)
        return attrs

    def validate_policies(self, data: dict) -> None:
        for policy in self.policies:
            policy(data)
