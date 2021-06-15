from ExpensesTracker.expenses.models import Expense


def calculate_money_left(profile):
    expenses = Expense.objects.all()
    total_expenses = sum(exp.price for exp in expenses) if expenses else 0
    return profile.budget - total_expenses
