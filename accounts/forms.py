from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Account

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

        help_texts = {
            'first_name': ("Please enter you first name"),
            'last_name': ("Please enter you last name"),
            'username': ("Please enter a username"),
            'email': ("Please enter a valid email address"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Please enter a password, it must be a mixture of letters and numbers'
        self.fields['password2'].help_text = 'Please re-enter your password'
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

        help_texts = {
            'first_name': ("Please change your first name if required"),
            'last_name': ("Please change your last name if required"),
            'email': ("Please change email address if required"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['last_name'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['email'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['password'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['password'].label = ""
        self.fields['password'].help_text = 'Raw passwords are not stored, so there is no way to see your user password, but you can change the password using the button below'

class ChangePasswordPageForm(PasswordChangeForm):
    class Meta:
        model = Account

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['new_password1'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['new_password2'].widget.attrs.update({'class': "form-label", 'class': "form-control"})
        self.fields['old_password'].label = "Old Password"
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Confirm new password"
        self.fields['old_password'].help_text = "Please enter your current password"
        self.fields['new_password2'].help_text = "Please re-enter your new password"       
        

    
      
        
    