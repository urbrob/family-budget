from budgets.application import use_cases, exceptions
from budgets.infrastructure.views import serializers
from rest_framework import permissions, views, status


class BudgetView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: views.Request) -> views.Response:
        serializer = serializers.CreateBudgetSerializer(data=request.data)
        if serializer.is_valid():
            request = use_cases.CreateBudgetUseCase.Request(
                name=serializer.validated_data['name'],
                user_id=request.user.id
            )
            use_cases.CreateBudgetUseCase().execute(request)
            return views.Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
        return views.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)