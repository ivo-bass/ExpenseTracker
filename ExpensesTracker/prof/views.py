from django.shortcuts import render, redirect

from ExpensesTracker.expenses.models import Expense
from ExpensesTracker.prof.forms import ProfileForm
from ExpensesTracker.prof.models import Profile
from ExpensesTracker.prof.utils import calculate_money_left


def show_profile(request):
    profile = Profile.objects.first()
    money_left = calculate_money_left(profile)
    context = {
        'profile': profile,
        'money_left': money_left,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            profile.save()
            return redirect(show_profile)
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.first()
        expenses = Expense.objects.all()
        profile.delete()
        [exp.delete() for exp in expenses]
        return redirect('/')
    return render(request, 'profile-delete.html')
