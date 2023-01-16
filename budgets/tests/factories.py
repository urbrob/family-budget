import factory

from budgets.domain import value_objects
from budgets.infrastructure import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Faker("first_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "pass")

class BudgetBalanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BudgetBalanceChange

    amount = factory.Faker("random_int")
    description = "Text"
    owner = factory.SubFactory(UserFactory)
    type = value_objects.BudgetBalanceChangeType.INCOME.value
    budget = factory.SubFactory("budgets.tests.factories.BudgetFactory")


class BudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Budget

    name = factory.Faker("name")
    owner = factory.SubFactory(UserFactory)


class BudgetMembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BudgetMembership

    budget = factory.SubFactory(BudgetFactory)
    user = factory.SubFactory(UserFactory)
    accepted = False
