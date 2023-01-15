from django.db import models as django_models


from budgets.infrastructure.models import mixins
from django.contrib.auth import get_user_model

User = get_user_model()


class BudgetMembership(mixins.CreateAndUpdateMixin, django_models.Model):
    user = django_models.ForeignKey(
        User, on_delete=django_models.CASCADE, related_name="shared_budgets"
    )
    budget = django_models.ForeignKey(
        'budgets.Budget', on_delete=django_models.CASCADE, related_name="shared_users"
    )
    accepted = django_models.BooleanField(default=False)