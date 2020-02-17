
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
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
            name='LeaveModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_Types', models.CharField(choices=[('SICK_LEAVE', 'SICK_LEAVE'), ('STUDY_LEAVE', 'STUDY_LEAVE'), ('EXAM_LEAVE', 'EXAM_LEAVE'), ('MATERNITY_LEAVE', 'MATERNITY_LEAVE'), ('PATERNITY_LEAVE', 'PATERNITY_LEAVE'), ('ANNUAL_LEAVE', 'ANNUAL_LEAVE'), ('COMPASSIONATE_LEAVE', 'COMPASSIONATE_LEAVE')], default='annual', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveClassDetails',
            fields=[
                ('Leave_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Leave_Type', models.CharField(choices=[(0, 'Approved'), (1, 'Pending'), (2, 'Declined'), (3, 'PendingCancellation')], max_length=1)),
                ('Begin_Date', models.DateField(help_text='Leave begin date')),
                ('End_Date', models.DateField(help_text='Leave end date')),
                ('Requested_Days', models.IntegerField(default=0, help_text='Total no of requested leave days')),
                ('Leave_Status', models.IntegerField(choices=[(0, 'Approved'), (1, 'Pending'), (2, 'Declined'), (3, 'PendingCancellation')], default=1)),
                ('Comments', models.CharField(max_length=500, null=True)),
                ('Coverage_Plans', models.CharField(max_length=50)),
                ('Leave_Attachments', models.FileField(upload_to='leave_management/media/leave_documents')),
                ('Submitted_Date', models.DateTimeField(auto_now_add=True)),
                ('Leave_Owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='employee.Employee')),
            ],
            options={
                'ordering': ('-Leave_Id',),
            },
        ),
    ]
