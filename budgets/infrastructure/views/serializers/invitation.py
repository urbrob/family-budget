from rest_framework import serializers

from budgets.application.policies import invitation as invitation_polcies
from budgets.infrastructure import models
from budgets.infrastructure.views.serializers import utils


class SendInvitationSerializer(utils.ModelWithPolicySerializer):
    policies = [
        invitation_polcies.user_is_not_an_owner_of_budget_policy,
        invitation_polcies.user_does_not_have_membership_to_budget_policy,
    ]
    email = serializers.CharField(required=True)
    budget_id = serializers.IntegerField(required=True)
    owner_id = serializers.IntegerField(required=True)

    def prepare_data_to_policies(self, attrs: dict) -> dict:
        try:
            attrs["user"] = models.User.objects.get(email=attrs["email"])
        except models.User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        return attrs

    class Meta:
        model = models.BudgetMembership
        fields = ("email", "budget_id", "owner_id")


class AcceptInvitationSerializer(utils.ModelWithPolicySerializer):
    policies = [
        invitation_polcies.user_is_owner_of_invitation_policy,
    ]
    invitation_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = models.BudgetMembership
        fields = ("invitation_id", "user_id")
