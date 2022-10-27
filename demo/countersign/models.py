from django.db import models
from viewflow.models import Process
from django.utils.translation import gettext_lazy as _
# Create your models here.

class cs_process(Process):
    #能上传，但不支持下载，可以自定义FORM模板下载
    file=models.FileField(_('countersigned文件'), upload_to = './upload/')
    version = models.CharField(_('Version'), max_length=50)
    mark = models.CharField(_('Remark'), max_length=1024)

    cfo_approved = models.CharField(
        max_length=1,
        choices=(
            ("1", "同意"),
            ("0", "不同意"),))

    ceo_approved = models.CharField(
        max_length=1,
        choices=(
            ("1", "同意"),
            ("0", "不同意"),))

    class Meta:
        verbose_name = _("countersigned")
        verbose_name_plural = _('countersigned')