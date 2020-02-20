# Generated by Django 3.0.2 on 2020-02-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_status', models.CharField(max_length=400, null=True)),
                ('comments', models.CharField(max_length=400, null=True)),
                ('coverage_plans', models.CharField(max_length=400, null=True)),
                ('department_team_lead', models.CharField(max_length=400, null=True)),
                ('employee', models.CharField(max_length=400, null=True)),
                ('employee_s_department', models.CharField(max_length=400, null=True)),
                ('HR_approve_cancellation', models.CharField(max_length=400, null=True)),
                ('leave_approved', models.CharField(max_length=400, null=True)),
                ('leave_end_date', models.CharField(max_length=400, null=True)),
                ('leave_entitlement_utilization', models.CharField(max_length=400, null=True)),
                ('leave_start_date', models.CharField(max_length=400, null=True)),
                ('leave_started', models.CharField(max_length=400, null=True)),
                ('leave_type', models.CharField(max_length=400, null=True)),
                ('line_manager_account', models.CharField(max_length=400, null=True)),
                ('line_manager_approve_cancellation', models.CharField(max_length=400, null=True)),
                ('next_step', models.CharField(max_length=400, null=True)),
                ('next_step_due_date', models.CharField(max_length=400, null=True)),
                ('no_of_approved_leave_days', models.CharField(max_length=400, null=True)),
                ('no_of_leave_days_requested', models.CharField(max_length=400, null=True)),
                ('request_from_VFP', models.CharField(max_length=400, null=True)),
                ('stage', models.CharField(max_length=400, null=True)),
                ('startEndDate', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leave_Entitlement_Type',
            fields=[
                ('Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Leave_Type', models.CharField(max_length=50)),
                ('Leave_Group', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveAccruals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days_Accrued', models.CharField(max_length=100)),
                ('Days_Worked', models.CharField(max_length=100, null=True)),
                ('Employee', models.CharField(blank=True, max_length=100)),
                ('Leave_Entitlement_Utilization', models.CharField(blank=True, max_length=100)),
                ('Period', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SanergyCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(blank=True, max_length=100, null=True)),
                ('Decsritption', models.CharField(blank=True, max_length=300, null=True)),
                ('isBusinessDay', models.BooleanField(blank=True, null=True)),
                ('isBusinessDayInclSat', models.BooleanField(blank=True, null=True)),
                ('isHoliday', models.BooleanField(blank=True, null=True)),
                ('isWeekend', models.BooleanField(blank=True, null=True)),
                ('isWeekend_or_Holiday', models.BooleanField(blank=True, null=True)),
                ('Weekday_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Weekday_No', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]