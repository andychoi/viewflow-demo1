from django.urls import re_path, include
from django.views import generic
from . import views

urlpatterns = [
    re_path('^$', generic.RedirectView.as_view(url='./employee/', permanent=False), name="index"),
    re_path('^employee/', include(views.EmployeeViewSet().urls)),
    re_path('^department/', include(views.DepartmentViewSet().urls)),
]