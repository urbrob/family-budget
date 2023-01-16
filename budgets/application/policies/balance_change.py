from budgets.infrastructure import models


def user_has_access_to_budget(data: dict) -> dict:
    if (
        not models.BudgetMembership.objects.filter(
            user=data["owner"], budget=data["budget"]
        ).exists()
        and not models.Budget.objects.filter(
            owner=data["owner"], id=data["budget"].id
        ).exists()
    ):
        raise Exception("User does not have access to budget.")
    return data
