from django.contrib import admin
from .models import User
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(forms.ModelForm):
    class Meta:
        widgets = {                          # Here
            'phone': PhoneNumberPrefixWidget(initial='BD'),
        }


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
