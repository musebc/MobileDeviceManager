from django.forms import ModelForm, PasswordInput, CharField, EmailInput
from django.contrib.auth.models import Group
from .models import PortalUser

class UserForm(ModelForm):
    """Form to create a general user."""
    email = CharField(label="Email", widget=EmailInput, required=True)
    password1 = CharField(label="Password", widget=PasswordInput, required=True)
    password2 = CharField(label="Repeat Password", widget=PasswordInput, required=True)

    class Meta:
        model = PortalUser
        fields = ['username', 'first_name', 'last_name', ]

class GroupForm(ModelForm):
    """Form that allows users to create a new group"""

    class Meta:
        model = Group
        fields = "__all__"
