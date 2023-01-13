from budgets.application import use_cases
from budgets.infrastructure.views import serializers
from budgets.infrastructure import models
from rest_framework import permissions, views, status, pagination


class BudgetView(views.APIView, pagination.LimitOffsetPagination):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: views.Request) -> views.Response:
        serializer = serializers.CreateBudgetSerializer(data=request.data)
        if serializer.is_valid():
            request = use_cases.CreateBudgetUseCase.Request(
                name=serializer.validated_data["name"], user_id=request.user.id
            )
            use_cases.CreateBudgetUseCase().execute(request)
            return views.Response({"status": "OK"}, status=status.HTTP_201_CREATED)
        return views.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: views.Request) -> views.Response:

        queryset = models.Budget.objects.filter(owner=request.user)
        if name := self.request.query_params.get("name"):
            queryset = queryset.filter(name=name)
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = serializers.BudgetSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
