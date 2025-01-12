# Generated by Django 4.1.2 on 2022-10-27 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_alter_department_options_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='passport_id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Working Address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='hr.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Work Mobile'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='notes',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_email',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Work Email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_location',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Office Location'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_phone',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Work Phone'),
        ),
    ]
