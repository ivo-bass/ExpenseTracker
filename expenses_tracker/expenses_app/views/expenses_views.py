from django.shortcuts import render, redirect

from expenses_tracker.expenses_app.forms.expense_form import ExpenseForm
from expenses_tracker.expenses_app.models import Expense
from expenses_tracker.expenses_app.views import index


def show_expense_form(request, form, template):
    context = {'form': form}
    return render(request, template, context)


def save_expense_form(request, form, template):
    if form.is_valid():
        form.save()
        return redirect(index)
    print(form.errors)
    return show_expense_form(request, form, template)


def create_expense(request):
    form = ExpenseForm()
    template = 'expense-create.html'
    if request.method == 'GET':
        return show_expense_form(request, form, template)
    form = ExpenseForm(request.POST)
    return save_expense_form(request, form, template)


def edit_expense(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)
    template = 'expense-edit.html'
    if request.method == 'GET':
        return show_expense_form(request, form, template)
    form = ExpenseForm(request.POST, instance=expense)
    return save_expense_form(request, form, template)



def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)
    template = 'expense-delete.html'
    if request.method == 'GET':
        for name, _ in form.fields.items():
            form.fields[name].widget.attrs['disabled'] = True
            form.save(commit=False)
        return show_expense_form(request, form, template)
    expense.delete()
    return redirect(index)
