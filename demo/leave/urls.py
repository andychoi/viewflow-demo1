from .views import *
from .flows import LeaveFlow
from django.urls import re_path, include
from django.views import generic


urlpatterns = [
    re_path('^$', generic.RedirectView.as_view(url='./leave/'), name="index"),
    re_path('^leave/', include(LeaveFlowViewSet(LeaveFlow).urls),name="leave"),
    re_path('^leave/action/delete/(?P<process_pk>\d+)/$',LeaveDel, name="delete"),
]
