from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from bugTracker_users.forms import LoginForm, NewUserForm
from bugTracker_users.models import TrackerUser

# Create your views here.


def login_view(request):
    # POST request handling
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_data = form.cleaned_data
            user = authenticate(
                request=request,
                credentials={
                    'username': login_data['username'],
                    'password': login_data['password']
                }
            )
            if user:
                # login creds provided are valid
                login(
                    request=request,
                    user=user
                )
                if request.GET.get('next'):
                    # redirect path provided with request
                    redirect_path = request.GET['next']
                    return HttpResponseRedirect(redirect_path)
                else:
                    # no redirect path with request
                    pass
                    '''
                    !!!!!! REDIRECT TO HOME PAGE, DO NOT FORGET THIS !!!!!!
                    '''
            else:
                # login creds are NOT valid
                form = LoginForm()
                return render(
                    request=request,
                    template_name='form.html',
                    context={
                        'page_title': 'Log In',
                        'button_value': 'Log In',
                        'form': form,
                        'error': 'Incorrect username and/or password',
                        'auth': request.user.is_authenticated
                    }
                )

    # GET request handling
    form = LoginForm()
    return render(
        request=request,
        template_name='form.html',
        context={
            'page_title': 'Log In',
            'button_value': 'Log In',
            'form': form,
            'auth': request.user.is_authenticated
        }
    )


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(
        reverse('login')
    )


@login_required
def new_user_view(request):
    # POST request handling
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            if user_data['password'] == user_data['confirm_password']:
                # password and password confirmation fields match
                new_user = TrackerUser.objects.create_user(
                    username=user_data['username'],
                    password=user_data['password'],
                    display_name=user_data['display_name']
                )
                new_user.save()
                '''
                !!!!!! REDIRECT TO HOME PAGE, DON'T FORGET THIS !!!!!!
                '''
            else:
                # password and password confirmation fields DO NOT match
                form = NewUserForm(initial={
                    'username': user_data['username'],
                    'display_name': user_data['display_name']
                })
                return render(
                    request=request,
                    template_name='form.html',
                    context={
                        'page_title': 'Create New User',
                        'button_value': 'Create',
                        'form': form,
                        'error': 'Password entries do not match',
                        'auth': request.user.is_authenticated
                    }
                )

    # GET request handling
    form = NewUserForm()
    return render(
        request=request,
        template_name='form.html',
        context={
            'page_title': 'Create New User',
            'button_value': 'Create',
            'form': form,
            'auth': request.user.is_authenticated
        }
    )


@login_required
def user_detail_view(request, userId):
    # GET request handling
    user = TrackerUser.objects.get(id=userId)
    if user.display_name:
        name = user.display_name
    else:
        name = user.username
    ''' 
    !!!!!! PARSE TICKETS BASED ON TICKET STATUS !!!!!!
        - TICKETS ASSIGNED TO USER
        - TICKETS FILED BY USER
        - TICKETS COMPLETED BY USER
    '''
    return render(
        request=request,
        template_name='userDetail.html',
        context={
            'name': name
        }
    )
