from django.shortcuts import render, redirect

from expenses_tracker.expenses_app.forms.profile_form import ProfileForm
from expenses_tracker.expenses_app.models import Profile, Expense


def show_profile_form(request, form, template):
    context = {'form': form}
    return render(request, template, context)


def save_profile_form(request, form, template):
    if form.is_valid():
        form.save()
        return redirect(index)
    return show_profile_form(request, form, template)


def home_no_profile(request):
    form = ProfileForm()
    template = 'home-no-profile.html'
    if request.method == "GET":
        return show_profile_form(request, form, template)
    form = ProfileForm(request.POST)
    return save_profile_form(request, form, template)


def home_with_profile(request):
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    context = {
        'profile': profile,
        'expenses': expenses,
    }
    return render(request, 'home-with-profile.html', context)


def index(request):
    profile = Profile.objects.first()
    if not profile:
        return home_no_profile(request)
    return home_with_profile(request)
