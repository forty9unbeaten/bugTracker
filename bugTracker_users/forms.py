import django.forms as forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=25, widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=50)
