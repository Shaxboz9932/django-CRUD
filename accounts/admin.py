from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        'username',
        'email',
        'age',
        'is_staff',
        'site'
    ]

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}), ('Web site', {"fields": ("site",)}),)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}), ('Web site', {"fields": ("site",)}),)


admin.site.register(CustomUser, CustomUserAdmin)

