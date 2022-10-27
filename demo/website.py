from django.urls import re_path
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .testing.models import TestingType


def users(request):
    return {
        'users': User.objects.filter(is_active=True).order_by('-username')
    }

def testing_types(request):
    return {
        'testing_types':TestingType.objects.all()
    }

def login_as(request):
    user = None

    user_pk = request.GET.get('user_pk', None)
    if user_pk:
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            pass

    username = request.GET.get('username', None)
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            pass

    if user:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
    else:
        logout(request)

    redirect_to = request.GET.get('next')
    if not redirect_to or not url_has_allowed_host_and_scheme(redirect_to):
        return redirect('/admin/testing/contract')
    else:
        return HttpResponseRedirect(redirect_to)


urlpatterns = [
    re_path(r'^login_as/$', login_as, name="login_as")
]
