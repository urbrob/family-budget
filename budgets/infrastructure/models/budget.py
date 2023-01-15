from django.db import models as django_models

from budgets.infrastructure.models import mixins
from budgets.infrastructure.models.budget_membership import BudgetMembership
from django.contrib.auth import get_user_model

User = get_user_model()


class Budget(mixins.CreateAndUpdateMixin, django_models.Model):
    user_members = django_models.ManyToManyField(User, through=BudgetMembership, related_name="shard_budgets")
    name = django_models.TextField()
    owner = django_models.ForeignKey(User, on_delete=django_models.CASCADE, related_name="budgets")
