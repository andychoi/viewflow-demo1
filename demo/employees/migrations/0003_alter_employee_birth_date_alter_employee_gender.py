# Generated by Django 4.1.2 on 2022-10-27 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_i18n'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=1, verbose_name='gender'),
        ),
    ]
