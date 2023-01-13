from django.db import models
from django.contrib.auth import get_user_model

from budgets.infrastructure.models import mixins

User = get_user_model()


class Budget(mixins.CreateAndUpdateMixin, models.Model):
    members = models.ManyToManyField(User, related_name="shard_budgets")
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
