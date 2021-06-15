from django.contrib import admin

from ExpensesTracker.prof.models import Profile


# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'budget']
