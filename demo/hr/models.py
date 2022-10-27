from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class employee(models.Model):

    birthday = models.DateTimeField(verbose_name=u"Date of Birth")
    # passport_id = models.CharField(verbose_name=u'passport No',max_length=1024, blank=True)
    sex = models.CharField(
        max_length=1,
        choices=(
            ("M", "Male"),
            ("F", "Female"),
            ("O", "Other")))
    marital= models.CharField(
        max_length=10,
        choices=(('single', 'Single'), ('married', 'Married'), ('widower', 'Widower'), ('divorced', 'Divorced')))
    department= models.ForeignKey('hr.department',related_name='member', on_delete=models.CASCADE, blank=True)
    address=models.CharField(verbose_name=u'Working Address',max_length=1024, blank=True)
    work_phone= models.CharField(verbose_name=u'Work Phone',max_length=1024, blank=True)
    mobile_phone= models.CharField(verbose_name=u'Work Mobile',max_length=1024, blank=True)
    work_email= models.CharField(verbose_name=u'Work Email',max_length=1024, blank=True)
    work_location= models.CharField(verbose_name=u'Office Location',max_length=1024, blank=True)
    notes= models.CharField(verbose_name=u'Notes',max_length=1024, blank=True)
    Manager=models.ForeignKey('hr.employee', blank=True, null=True, related_name='lead_member', on_delete=models.CASCADE,)

    #
    user = models.OneToOneField(User, verbose_name=u"account binding", on_delete=models.CASCADE, blank=True)
    # image: all image fields are base64 encoded and PIL-supported
    #image=models.ImageField(verbose_name=u"Photo")
    class Meta:
        db_table = 'hr.employee'
        verbose_name = 'employee'
        verbose_name_plural = "Employee"

    def __str__(self):
        return self.user.username

class department(models.Model):

    class Meta:
        db_table = 'hr.department'
        verbose_name = 'department'
        verbose_name_plural = "Department"

    name = models.CharField(verbose_name=u'Department Name',max_length=1024)
    parent = models.ForeignKey('hr.department', blank=True, null=True, related_name='dep_children', on_delete=models.CASCADE,)
    leader = models.ForeignKey('hr.employee', blank=True, null=True, related_name='emp_children', on_delete=models.CASCADE,)
    note=models.CharField(verbose_name=u'Note',max_length=1024)


    def __str__(self):
    # dep_tree = _get_dep_tree(self)
        return self.name
    #
    # def _get_dep_tree(self):
    # ret = ''
    # if (self.parent is not None):
    # ret = _get_dep_tree(self.parent)
    #
    # return ret + '/'+dep.name