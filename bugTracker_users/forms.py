import django.forms as forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
