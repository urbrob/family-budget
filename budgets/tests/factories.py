import factory

from budgets.infrastructure import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Faker('first_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'pass')