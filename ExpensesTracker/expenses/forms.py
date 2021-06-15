from django import forms

from ExpensesTracker.expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'title',
            'image_url',
            'description',
            'price',
        ]
        widgets = {
            'title': forms.TextInput(),
            'image_url': forms.URLInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput()
        }