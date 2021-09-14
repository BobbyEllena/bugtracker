from django import forms
from django.contrib.auth.forms import UserCreationForm
from bug.models import BugModel, CustUser

class CreateUser(UserCreationForm):
    class Meta:
        model = CustUser
        fields = [
            'username',
            'password',
            'display_name',
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class BugForm(forms.ModelForm):
    class Meta:
        model = BugModel
        fields = [
            'title',
            'description',
        ]




