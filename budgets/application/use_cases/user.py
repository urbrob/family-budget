from dataclasses import dataclass

from budgets.application import exceptions
from budgets.infrastructure import models


class RegisterUserUseCase:
    @dataclass
    class Request:
        username: str
        email: str
        password: str

    def execute(self, request: Request) -> None:
        if models.User.objects.filter(email=request.email).exists():
            raise exceptions.UserAlreadyExist
        models.User.objects.create_user(username=request.username, email=request.email, password=request.password)