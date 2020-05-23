from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm


MyUser=get_user_model()

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=('username', 'email', 'date_of_birth', 'is_admin')
    list_filter=('is_admin',)
    fieldsets=(
        (None, {'fields':('username', 'email', 'password')}),
        ('Personnal info', {'fields':('date_of_birth', 'profile_image')}),
        ('Permissions', {'fields':('is_admin',)}),
    )

    add_fieldsets=(
        (None, {
            'classes':('wide',),
            'fields':('email', 'date_of_birth', 'password1', 'password2'),

        }),
    )
    search_fields=('email',)
    ordering=('email',)
    filter_horizontal=()

admin.site.register(MyUser, UserAdmin)
