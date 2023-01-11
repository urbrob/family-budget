from budgets.domain.value_objects import enum


class BudgetBalanceChangeType(enum.ChoiceEnum):
    INCOME = 'INCOME'
    EXPENSE = 'EXPENSE'


