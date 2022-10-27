# Generated by Django 4.1.2 on 2022-10-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20171130_0922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leave_class',
            options={'verbose_name': 'Leave category', 'verbose_name_plural': 'Leave category'},
        ),
        migrations.AlterModelOptions(
            name='leaveprocess',
            options={'verbose_name': 'leave process', 'verbose_name_plural': 'leave process'},
        ),
        migrations.AlterField(
            model_name='leaveprocess',
            name='dep_approved',
            field=models.IntegerField(default=0, verbose_name='department review'),
        ),
        migrations.AlterField(
            model_name='leaveprocess',
            name='dep_approved_comment',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='department leader review comments'),
        ),
        migrations.AlterField(
            model_name='leaveprocess',
            name='dep_approved_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Department Leader Review Time'),
        ),
        migrations.AlterField(
            model_name='leaveprocess',
            name='hr_approved',
            field=models.IntegerField(default=0, verbose_name='Personnel Audit'),
        ),
        migrations.AlterField(
            model_name='leaveprocess',
            name='hr_approved_comment',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Personnel review comments'),
        ),
        migrations.AlterField(
            model_name='leaveprocess',
            name='hr_approved_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Personnel review time'),
        ),
    ]