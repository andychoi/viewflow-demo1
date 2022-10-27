import django
# from django.conf.urls import include, url
from django.urls import re_path, include
from django.contrib import admin
from django.contrib.auth import views as auth
from django.views import generic

from material import frontend
from material.frontend.apps import ModuleMixin
from material.frontend.registry import modules



class Demo(ModuleMixin):
    """
    Home page module
    """
    order = 1
    label = 'Introduction'
    verbose_name = 'Introduction'
    icon = '<i class="material-icons">account_balance</i>'

    @property
    def urls(self):
        index_view = generic.TemplateView.as_view(template_name='demo/index.html')

        return frontend.ModuleURLResolver(
            '^', [re_path('^$', index_view, name="index")],
            module=self, app_name='demo', namespace='demo')

    def index_url(self):
        return '/'

    def installed(self):
        return True

modules.register(Demo())



if django.VERSION < (1, 7):
    admin.autodiscover()


from material.frontend import urls as frontend_urls  # NOQA

urlpatterns = [
    re_path(r'^accounts/login/$', auth.LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$', auth.LogoutView.as_view(), name='logout'),
    re_path(r'^', include('demo.website')),
    re_path(r'', include(frontend_urls)),
]
