from django import test
from django.db import models

class BaseTest(test.TestCase):
    def assertModelExist(self, model_class: models.Model, **params) -> None:
        record = model_class.objects.filter(**params).exists()
        self.assertTrue(record)

    def assertModelNotExist(self, model_class: models.Model, **params) -> None:
        record = model_class.objects.filter(**params).exists()
        self.assertFalse(record)