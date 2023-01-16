from budgets.domain.value_objects import enum


class BudgetBalanceChangeCategory(enum.ChoiceEnum):
    OTHER = "OTHER"
    GROCERY = "GROCERY"
    TAXES = "TAXES"

