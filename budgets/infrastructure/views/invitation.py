from budgets.application import use_cases
from budgets.infrastructure import models
from budgets.infrastructure.views import serializers
from rest_framework import permissions, views, status, pagination


class InvitationView(views.APIView, pagination.LimitOffsetPagination):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: views.Request) -> views.Response:
        data = {
            "email": request.data.get("email"),
            "budget_id": request.data.get("budget_id"),
            "owner_id": request.user.id,
        }
        serializer = serializers.SendInvitationSerializer(data=data)
        if serializer.is_valid():

            request = use_cases.SendInvitationUseCase.Request(
                budget_id=serializer.validated_data["budget_id"],
                user_id=serializer.validated_data["user"].id,
            )
            use_cases.SendInvitationUseCase().execute(request)
            return views.Response({"status": "OK"}, status=status.HTTP_201_CREATED)
        return views.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: views.Request) -> views.Response:
        data = {
            "user_id": request.user.id,
            "invitation_id": request.data.get("invitation_id"),
        }
        serializer = serializers.AcceptInvitationSerializer(data=data)
        if serializer.is_valid():
            request = use_cases.AcceptInvitationUseCase.Request(
                invitation_id=serializer.validated_data["invitation_id"]
            )
            use_cases.AcceptInvitationUseCase().execute(request)
            return views.Response({"status": "OK"}, status=status.HTTP_201_CREATED)
        return views.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: views.Request) -> views.Response:
        queryset = models.BudgetMembership.objects.filter(user=request.user)
        if name := self.request.query_params.get("name"):
            queryset = queryset.filter(budget__name=name)
        if activated := self.request.query_params.get("activated"):
            queryset = queryset.filter(activated=activated)

        results = self.paginate_queryset(queryset, request, view=self)
        serializer = serializers.InvitationSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
