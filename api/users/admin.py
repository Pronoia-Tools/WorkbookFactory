from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import identify_hasher, UNUSABLE_PASSWORD_PREFIX
from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join, mark_safe
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Account, Subscription


class ReadOnlyPasswordHashWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        encoded = value
        final_attrs = self.build_attrs(attrs)

        if not encoded or encoded.startswith(UNUSABLE_PASSWORD_PREFIX):
            summary = mark_safe("<strong>%s</strong>" %
                                ugettext("No password set."))
        else:
            try:
                hasher = identify_hasher(encoded)
            except ValueError:
                summary = mark_safe(
                    "<strong>%s</strong>"
                    % ugettext("Invalid password format or unknown hashing algorithm.")
                )
            else:
                summary = format_html_join(
                    "",
                    "<strong>{}</strong>: {} ",
                    (
                        (ugettext(key), value)
                        for key, value in hasher.safe_summary(encoded).items()
                    ),
                )

        return format_html("<div{}>{}</div>", flatatt(final_attrs), summary)


class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("required", False)
        super(ReadOnlyPasswordHashField, self).__init__(*args, **kwargs)

    def bound_data(self, data, initial):
        # Always return initial because the widget doesn't
        # render an input field.
        return initial

    def has_changed(self, initial, data):
        return False


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ("username", "email",)


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ("username", "email", "password")

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AccountAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    list_display = ("email", "created", "opt_in",)
    add_form = AccountCreationForm
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "opt_in",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        )
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    ordering = ("email",)


admin.site.register(Account, AccountAdmin)
admin.site.register(Subscription)
