from django.contrib import admin

from ExpensesTracker.expenses.models import Expense

# admin.site.register(Expense)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
