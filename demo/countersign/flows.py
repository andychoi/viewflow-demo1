import os
from django.utils.translation import gettext_lazy as _

from viewflow import flow, frontend, lock
from viewflow.base import this, Flow
from viewflow.flow import views as flow_views


from .models import cs_process


@frontend.register
class CSFlow(Flow):
    """
    并行countersigneddemo
    动态拆分见作者自带的customnode列子。
    """
    process_class = cs_process
    process_title = _('countersigned')
    process_description = _('countersigned演示.')

    lock_impl = lock.select_for_update_lock

    summary_template = _("'{{ process.mark }}' countersigned")

    start = (
        flow.Start(
            flow_views.CreateProcessView,
            fields=['file','mark','version'],
            task_title=_('New countersigned'))
        .Permission(auto_create=True)
        .Next(this.split_sign)
    )

    split_sign=(
        flow.Split(
            task_title=_('并行countersigned')
        )
        .Next(this.cfo_sign)
        .Next(this.ceo_sign)
    )

    #财务官countersigned
    cfo_sign=(
        flow.View(
            flow_views.UpdateProcessView, fields=['file','mark','cfo_approved'],
            task_title=_('CFO countersigned'),
            task_result_summary = _("CFO{% ifequal process.cfo_approved '1' %} 同意 {% else %}不同意{% endifequal %}")
        )
        .Permission(auto_create=True)
        .Next(this.join_on_sign)
    )

    #CEOcountersigned
    ceo_sign=(
        flow.View(
            flow_views.UpdateProcessView, fields=['file','mark','ceo_approved'],
            task_title=_('CEO countersigned'),
            task_result_summary = _("CEO{% if process.ceo_approved == '1' %} 同意 {% else %}不同意{% endif %}")
        )
        .Permission(auto_create=True)
        .Next(this.join_on_sign)
    )

    join_on_sign = (
        flow.Join(
            task_title=_('等待所有countersigned结束')
        ).Next(this.decision)
    )
    #一票否决制。
    decision = (
        flow.If(
            cond=lambda act: act.process.cfo_approved=='1' and act.process.ceo_approved=='1',
            task_title=_('countersigned结果'),
            task_result_summary=_("countersigned结果{% if process.ceo_approved == '1' and  process.cfo_approved == '1'%} 通过 {% else %}不通过{% endif %}")
        )
        .Then(this.OK)
        .Else(this.NG)
    )

    NG = (
        flow.Handler(
            this.send_NG_request
        ).Next(this.end)
    )

    OK = (
        flow.Handler(
            this.send_OK_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_NG_request(self, activation):
        print('ceo_approved==>'+ str(activation.process.ceo_approved))
        print('cfo_approved==>' + str(activation.process.cfo_approved))
        print('NG')

    def send_OK_request(self, activation):
        print('OK')