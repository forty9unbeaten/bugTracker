from django.shortcuts import render
from bugTracker_users.forms import LoginForm

# Create your views here.


def login_view(request):
    # GET request handling
    form = LoginForm()
    html = 'form.html'
    return render(
        request,
        html,
        {
            'page_title': 'Log In',
            'button_value': 'Log In',
            'form': form
        }
    )
