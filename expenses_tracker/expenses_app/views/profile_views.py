from django.shortcuts import render, redirect

from expenses_tracker.expenses_app.forms.profile_form import ProfileForm
from expenses_tracker.expenses_app.models import Profile, Expense
from expenses_tracker.expenses_app.views import index, show_profile_form, save_profile_form


def index_profile(request):
    profile = Profile.objects.first()
    template = 'profile.html'
    return show_profile_form(request, form=profile, template=template)


def edit_profile(request):
    profile = Profile.objects.first()
    form = ProfileForm(instance=profile)
    template = 'profile-edit.html'
    if request.method == 'GET':
        return show_profile_form(request, form, template=template)
    form = ProfileForm(request.POST, instance=profile)
    return save_profile_form(request, form, template)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    profile.delete()
    for exp in Expense.objects.all():
        exp.delete()
    return redirect(index)
