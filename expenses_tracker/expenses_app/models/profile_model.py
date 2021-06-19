from django.core.validators import MinValueValidator
from django.db import models

from .expense_model import Expense
from expenses_tracker.validators import validate_integer


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15
    )
    last_name = models.CharField(
        max_length=15
    )
    budget = models.IntegerField(
        validators=(
            MinValueValidator(1),
        )
    )

    def money_left(self):
        total_expenses = sum(exp.price for exp in Expense.objects.all())
        return self.budget - total_expenses
