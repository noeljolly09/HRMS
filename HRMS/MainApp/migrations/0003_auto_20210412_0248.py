# Generated by Django 3.2 on 2021-04-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20210412_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='DOB',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='phoneNumber',
            field=models.IntegerField(default=None),
        ),
    ]
