import factory

from budgets.infrastructure import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Faker("first_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "pass")


class BudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Budget

    name = factory.Faker("name")
    owner = factory.SubFactory(UserFactory)
