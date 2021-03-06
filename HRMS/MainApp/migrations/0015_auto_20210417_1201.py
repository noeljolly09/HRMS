# Generated by Django 2.2.13 on 2021-04-17 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0014_auto_20210417_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='leave',
        ),
        migrations.AddField(
            model_name='leave',
            name='employee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.employeeDetails'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('approved', 'APPROVED'), ('unapproved', 'UNAPPROVED'), ('decline', 'DECLINED')], default='Un Approved', max_length=15),
        ),
    ]
