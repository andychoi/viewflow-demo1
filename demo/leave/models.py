from django.db import models
from viewflow.models import Process
from demo.hr.models import *


class Leave_class(models.Model):
    name= models.CharField(max_length=256, verbose_name=u"名称")
    class Meta:
        db_table = 'leave_class'
        verbose_name = 'Leave category'
        verbose_name_plural = "Leave category"



    def __str__(self):
        return self.name


# class department(models.Model):
#     name = models.CharField(max_length=256, verbose_name=u"名称")
#     leader = models.ForeignKey(User, verbose_name=u"Department经理")
#
#     class Meta:
#         db_table = 'department'
#         verbose_name = 'Department'
#         verbose_name_plural = "Department"
#
#     def __str__(self):
#         return self.name

class Leave(models.Model):
    """leave内容"""
    req_by = models.ForeignKey(employee, verbose_name=u"申请人", on_delete=models.CASCADE,)
    req_date = models.DateTimeField(verbose_name=u"申请时间")
    depart_name = models.ForeignKey(department,verbose_name=u'Department', on_delete=models.CASCADE,)
    position =  models.CharField(max_length=256,  verbose_name=u"职位")
    req_class =models.ForeignKey(Leave_class,verbose_name=u'leave类别', on_delete=models.CASCADE,)
    start_time=models.DateTimeField(verbose_name=u"开始时间")
    end_time=models.DateTimeField(verbose_name=u"结束时间")
    resion=models.CharField(max_length=256,  verbose_name=u"leave事由")
    file_url=models.CharField(max_length=256,  verbose_name=u"上传附件")
    comment = models.CharField(max_length=256, verbose_name=u"Remark",blank=True,null=True)
    #审批领导

    class Meta:
        db_table = 'leave'
        verbose_name = 'leave'
        verbose_name_plural = "leave"

    def __str__(self):
        return self.req_by.user.username


class LeaveProcess(Process):

    leave = models.OneToOneField(Leave,null=True,blank=True, on_delete=models.CASCADE,)

    dep_approved = models.IntegerField(default=0, verbose_name=u"department review")
    dep_approved_time = models.DateTimeField(verbose_name=u"Department Leader Review Time",blank=True,null=True)
    dep_approved_comment = models.CharField(max_length=256, verbose_name=u"department leader review comments",blank=True,null=True)

    hr_approved = models.IntegerField(default=0, verbose_name=u"Personnel Audit")
    hr_approved_time = models.DateTimeField(verbose_name=u"Personnel review time",blank=True,null=True)
    hr_approved_comment= models.CharField(max_length=256, verbose_name=u"Personnel review comments",blank=True,null=True)
    comment=models.CharField(max_length=1024,blank=True,null=True)

    class Meta:
        db_table = 'leave_process'
        verbose_name = 'leave process'
        verbose_name_plural = "leave process"
