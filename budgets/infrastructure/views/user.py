from budgets.application import use_cases, exceptions
from budgets.infrastructure.views import serializers
from rest_framework import permissions, views, status


class UserRegistrationView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request: views.Request) -> views.Response:
        serializer = serializers.UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            request = use_cases.RegisterUserUseCase.Request(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                username=serializer.validated_data['username']
            )
            try:
                use_cases.RegisterUserUseCase().execute(request)
            except exceptions.UserAlreadyExist:
                return views.Response({'email': 'Email already taken!'}, status=status.HTTP_400_BAD_REQUEST)
            return views.Response({'status': 'OK'}, status=status.HTTP_201_CREATED)
        return views.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)