from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Account
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

        labels = {
           'first_name': _("First Name"),
           'last_name': _("Last Name"),
           'user_name': _("Username"),
           'email': _("Email"),
        }

        help_texts = {
            'first_name': _("Please enter you first name"),
            'last_name': _("Please enter you last name"),
            'username': _("Please enter a username"),
            'email': _("Please enter a valid email address"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('Please enter a password, it must be a mixture of letters and numbers')
        self.fields['password2'].help_text = _('Please re-enter your password')
        self.fields['first_name'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['last_name'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['username'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['email'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['password1'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['password2'].widget.attrs.update({'class': "form-label", 'class': "form-control"})

class EditProfilePageForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ("first_name", "last_name","email")

        labels = {
           'first_name': _("First Name"),
           'last_name': _("Last Name"),
           'email': _("Email"),
        }

        help_texts = {
            'first_name': _("Please change your first name if required"),
            'last_name': _("Please change your last name if required"),
            'email': _("Please change email address if required"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['last_name'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['email'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['password'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['password'].label = ""
        self.fields['password'].help_text = _('Raw passwords are not stored, so there is no way to see your user password, but you can change the password using the button below')

class ChangePasswordPageForm(PasswordChangeForm):
    class Meta:
        model = Account

        labels = {
           'old_password': _("Old Password"),
           'new_password1': _("New Password"),
           'new_password2': _("Confirm new password"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['new_password1'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['new_password2'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['old_password'].help_text = _("Please enter your current password")
        self.fields['new_password2'].help_text = _("Please re-enter your new password")   
        
        
    