# Generated by Django 3.0.2 on 2020-03-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management', '0002_sanergydepartment_sanergydepartmentunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanergydepartment',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanergydepartmentunit',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]