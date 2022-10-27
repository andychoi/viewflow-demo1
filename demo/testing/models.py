from django.db import models
from django.contrib.auth.models import User



class TestingStandard(models.Model):


    name =models.CharField(max_length=10,  verbose_name=u"Standard名称")
    no = models.CharField(max_length=10,  verbose_name=u"协议号")
    st_class = models.CharField(max_length=1, verbose_name=u"Standard类别",choices=(
            ("0", "国标"),
            ("1", "行标"),
            ("2", "企标")))
    class Meta:
        verbose_name = 'Standard'
        verbose_name_plural = "Standard"


    def __str__(self):
        stardard_class = {'0': '国标', '1': '行标', '2': '企标'}
        return stardard_class[self.st_class] +" | "+ self.name

class TestingType(models.Model):
    name = models.CharField(max_length=1024,  verbose_name=u"Test Type")
    mark = models.CharField(max_length=1024,  verbose_name=u"Remark")

    class Meta:
        verbose_name = 'Test Type'
        verbose_name_plural = "Test Type"

    def __str__(self):
        return self.name

class TestingItem(models.Model):
    name = models.CharField(max_length=10,  verbose_name=u"测试项名称")
    #standard = models.ForeignKey(TestingStandard, verbose_name=u"Standard类别")
    testing_type = models.ForeignKey(TestingType, verbose_name=u"Standard类别",  on_delete=models.CASCADE,)
    class Meta:
        verbose_name = 'Test items'
        verbose_name_plural = "Test items"


    def __str__(self):
        return self.name

class TestingItemTemp(models.Model):
    name = models.CharField(max_length=10,  verbose_name=u"模板名称")
    items = models.ManyToManyField(TestingItem,verbose_name=u"Test items")
    class Meta:
        verbose_name = 'Test items模板'
        verbose_name_plural = "Test items模板"


    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=1024,  verbose_name=u"单位名称")
    address = models.CharField(max_length=1024,  verbose_name=u"单位地址")
    telephone = models.CharField(max_length=1024,  verbose_name=u"电话")
    atten =  models.CharField(max_length=1024,  verbose_name=u"联系人")
    postcode = models.CharField(max_length=1024,  verbose_name=u"邮编")
    fax =  models.CharField(max_length=1024,  verbose_name=u"传真")


    class Meta:
        verbose_name = 'Requester'
        verbose_name_plural = "Requester"


    def __str__(self):
        return self.name

# Create your models here.
class Contract(models.Model):
    protocol_no = models.CharField(max_length=10,  verbose_name=u"Agreement编号")
    task_no = models.CharField(max_length=10,  verbose_name=u"任务流水号")
    product_type = models.CharField(max_length=1024,  verbose_name=u"产品名称/规格型号")
    product_num = models.IntegerField( verbose_name=u"数量")
    customer = models.ForeignKey(Customer,related_name='contracts',verbose_name=u"Requester",  on_delete=models.CASCADE,)
    sample_from = models.CharField(max_length=1, verbose_name=u"来样方式")
    sample_to = models.CharField(max_length=1, verbose_name=u"样品处理")
    report_get = models.CharField(max_length=1, verbose_name=u"报告领取")
    testing_area = models.CharField(max_length=1, verbose_name=u"测试地点")
    report_num = models.IntegerField( verbose_name=u"报告份数",help_text='份数')
    testing_class = models.CharField(max_length=1, verbose_name=u"检测类别")
    testing_time_class = models.CharField(max_length=1, verbose_name=u"检测时间")
    testing_time = models.IntegerField( verbose_name=u"加急",null =True,blank= True,help_text='工作日')
    testing_standards = models.ManyToManyField(TestingStandard,verbose_name=u"检测依据")
    testing_items = models.ManyToManyField(TestingItem,verbose_name=u"Test items")
    testing_fee = models.FloatField(verbose_name='测试费用',help_text='元',)
    testing_fee_tax_no = models.CharField(max_length=1024, verbose_name=u"发票号")
    testing_fee_tax_class = models.CharField(max_length=1, verbose_name=u"发票类别")
    testing_status = models.CharField(max_length=1, verbose_name=u"检测状态")
    testing_type = models.ForeignKey(TestingType, verbose_name=u"Standard类别",  on_delete=models.CASCADE,)
    create_user  = models.ForeignKey(User,verbose_name=u"创建人",  on_delete=models.CASCADE,)
    create_datetime = models.DateTimeField( verbose_name=u"创建日期")

    class Meta:
        verbose_name = 'Agreement'
        verbose_name_plural = "Agreement"


    def __str__(self):
        return self.protocol_no

