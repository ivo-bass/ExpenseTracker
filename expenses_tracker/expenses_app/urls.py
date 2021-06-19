from django.urls import path

from expenses_tracker.expenses_app.views import index, create_expense, edit_expense, delete_expense, index_profile, \
    edit_profile, delete_profile

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_expense, name="create expense"),
    path('edit/<int:id>', edit_expense, name="edit expense"),
    path('delete_expense<int:id>', delete_expense, name="delete expense"),
    path('profile/', index_profile, name="index profile"),
    path('profile/edit/', edit_profile, name="edit profile"),
    path('profile/delete/', delete_profile, name="delete profile"),
]
