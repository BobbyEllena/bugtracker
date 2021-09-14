from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bug.models import BugModel, CustUser
from bug.forms import LoginForm, CreateUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CreateUser
    form = CreateUser
    model = CustUser
    list_display = ['email', 'username',]


admin.site.register(BugModel)
admin.site.register(CustUser)