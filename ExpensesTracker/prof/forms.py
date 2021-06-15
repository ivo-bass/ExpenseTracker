from django import forms

from ExpensesTracker.prof.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'budget',
            'first_name',
            'last_name',
        ]
        widgets = {
            'budget': forms.NumberInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput()
        }