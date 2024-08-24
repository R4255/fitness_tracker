from django.urls import path
from . import views
from allauth.account.views import PasswordResetFromKeyView

urlpatterns = [
    path('', views.index, name='index'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('calculate_bmi/', views.calculate_bmi, name='calculate_bmi'),
    path('add_diet_entry/', views.add_diet_entry, name='add_diet_entry'),
    path('calory_track/', views.calory_track, name='calory_track'),
    # Remove the signup URL as it's now handled by allauth
    path('delete_workout/<int:pk>/', views.delete_workout, name='delete_workout'),
    path('accounts/password/reset/key/<uidb36>-<key>/', PasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
]