from django import test
from django.db import models
from budgets.tests import factories


class BaseTest(test.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = factories.UserFactory()

    def assertModelExist(self, model_class: models.Model, **params) -> None:
        record = model_class.objects.filter(**params).exists()
        self.assertTrue(record)

    def assertModelNotExist(self, model_class: models.Model, **params) -> None:
        record = model_class.objects.filter(**params).exists()
        self.assertFalse(record)
