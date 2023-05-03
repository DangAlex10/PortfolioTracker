from django.contrib import admin
from django.contrib.auth.models import User
from webpage.models import UserProfile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserProfioleInLine(admin.StackedInline):
    model = UserProfile
    can_delete = True

class AccountsUserAdmin(AuthUserAdmin):
    inlines = [UserProfioleInLine]

admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)