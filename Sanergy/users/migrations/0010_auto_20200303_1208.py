# Generated by Django 3.0.2 on 2020-03-03 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200303_0457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('email',)},
        ),
    ]
