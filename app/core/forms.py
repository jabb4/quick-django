from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Username", "type": "text", "autofocus": "autofocus"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password", "type": "password"}))


class CreateUserForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Username", "type": "text", "autocomplete": "off", "autofocus": "autofocus"}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password", "autocomplete": "off", "type": "password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Repeat Password", "autocomplete": "off", "type": "password"}))

    class Meta:
        model = get_user_model()
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class DeleteUserForm(forms.Form):
    delete_user_password = forms.CharField(widget=forms.TextInput(
        attrs={"label": "Current Password", "placeholder": "Current Password", "type": "password"}))
