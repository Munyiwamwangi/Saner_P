# Generated by Django 3.0.2 on 2020-03-19 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Employee_First_Name', models.CharField(max_length=100, null=True)),
                ('Employee_Last_Name', models.CharField(max_length=100, null=True)),
                ('Employee_Full_Name', models.CharField(max_length=100)),
                ('Company_Division', models.CharField(blank=True, max_length=100)),
                ('Sanergy_Department', models.CharField(max_length=100, null=True)),
                ('Sanergy_Department_Unit', models.CharField(max_length=100, null=True)),
                ('Employee_Active', models.BooleanField(default=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('IsDeleted', models.BooleanField(null=True)),
                ('Image', models.FileField(default='default.jpg', upload_to='profile_pics')),
                ('Date_Of_Birth', models.DateField(default=django.utils.timezone.now)),
                ('Joined_Date', models.DateField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False, null=True)),
                ('is_employee', models.BooleanField(default=True, null=True)),
                ('HR_Employee_ID', models.CharField(max_length=100, null=True, unique=True)),
                ('Leave_Group', models.CharField(max_length=100, null=True)),
                ('Employee_Role', models.CharField(max_length=100, null=True)),
                ('Primary_Phone', models.CharField(blank=True, max_length=100, null=True)),
                ('Line_Manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='line_manager', to='employee.Employee')),
                ('Talent_Partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='talent_partner', to='employee.Employee')),
                ('Team_Lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='team_lead', to='employee.Employee')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('Employee_Full_Name',),
            },
        ),
    ]
