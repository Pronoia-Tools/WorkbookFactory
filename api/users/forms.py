from django import forms
from users.models import Account, Subscription
from allauth.account.models import EmailAddress


class UsernameForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', ]


class NameForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['subscribed']


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['email', ]


class PrimaryForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['primary', ]


class SignupForm(forms.Form):
    opt_in = forms.BooleanField(label="Add me to the Workbok Factory email list", help_text="Don't worry. We won't spam you.", initial=True, required=False)

    def signup(self, request, user):
        user.opt_in = self.cleaned_data['opt_in']
        user.save()