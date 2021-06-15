from django.shortcuts import render, redirect

from ExpensesTracker.expenses.forms import ExpenseForm
from ExpensesTracker.expenses.models import Expense
from ExpensesTracker.prof.forms import ProfileForm
from ExpensesTracker.prof.models import Profile
from ExpensesTracker.prof.views import calculate_money_left


def index_no_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
        return render(request, 'home-no-profile.html', {'form': form})
    form = ProfileForm(request.POST)
    if form.is_valid():
        profile = form.save()
        profile.save()
    return redirect(index)


def index_with_profile(request, profile):
    expenses = Expense.objects.all()
    money_left = calculate_money_left(profile)

    context = {
        'money_left': money_left,
        'profile': profile,
        'expenses': expenses,
    }
    return render(request, 'home-with-profile.html', context)


def index(request):
    profile = Profile.objects.first()
    if profile:
        return index_with_profile(request, profile)
    else:
        return index_no_profile(request)




def create_expense(request):
    if request.method == 'GET':
        form = ExpenseForm()
        return render(request, 'expense-create.html', {'form': form})
    form = ExpenseForm(request.POST)
    if form.is_valid():
        expense = form.save()
        expense.save()
    return redirect(index)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save()
            expense.save()
            return redirect(index)
    else:
        form = ExpenseForm(instance=expense)

    context = {'form': form}
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        expense.delete()
        return redirect(index)
    else:
        form = ExpenseForm(instance=expense)
        form.fields['title'].widget.attrs['readonly'] = True
        form.fields['description'].widget.attrs['readonly'] = True
        form.fields['image_url'].widget.attrs['readonly'] = True
        form.fields['price'].widget.attrs['readonly'] = True

    context = {'form': form}
    return render(request, 'expense-delete.html', context)
