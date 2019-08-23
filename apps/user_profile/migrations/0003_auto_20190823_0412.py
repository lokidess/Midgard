# Generated by Django 2.2.4 on 2019-08-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20190823_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Отчество'),
        ),
    ]
