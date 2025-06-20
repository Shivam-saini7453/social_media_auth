from django import forms
from django.utils.functional import lazy
from django.utils.module_loading import import_string

# Lazy load the SignupForm to avoid circular import
def get_signup_form():
    return import_string('allauth.account.forms.SignupForm')

class CustomSignupForm(get_signup_form()):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
