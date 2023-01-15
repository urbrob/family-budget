from budgets.infrastructure import models


def budget_belongs_to_user_policy(data: dict) -> None:
    if not models.Budget.objects.filter(
        id=data["id"], owner_id=data["owner_id"]
    ).exists():
        raise Exception("Budget does not exist.")
    return data
