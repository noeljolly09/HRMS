# Generated by Django 3.2 on 2021-04-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='address',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='email',
            field=models.EmailField(default=None, max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='firstName',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='lastName',
            field=models.CharField(default=None, max_length=20),
        ),
    ]