# Generated by Django 2.2.13 on 2021-04-16 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_auto_20210417_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='Name',
        ),
    ]
