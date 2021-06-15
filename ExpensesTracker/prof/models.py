from django.db import models

from ExpensesTracker.expenses.models import Expense


# def calculate_budget():
#     profile = Profile.objects.all().first()
#     expenses = Expense.objects.all()
#     total_expenses = sum(exp.price for exp in expenses) if expenses else 0
#     return profile.budget - total_expenses


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
    )
    last_name = models.CharField(
        max_length=15,
    )
    budget = models.IntegerField()

    # calculated_budget = calculate_budget()