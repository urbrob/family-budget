from budgets.infrastructure import models


def user_does_not_have_membership_to_budget_policy(data: dict) -> None:
    if models.BudgetMembership.objects.filter(user_id=data['user'].id, budget_id=data['budget_id']).exists():
        raise Exception('User is already invited to given budget.')
    return data

def user_is_not_an_owner_of_budget_policy(data: dict) -> None:
    if not models.Budget.objects.filter(owner_id=data['owner_id'], id=data['budget_id']).exists():
        raise Exception('User is not an owner of Budget')
    return data