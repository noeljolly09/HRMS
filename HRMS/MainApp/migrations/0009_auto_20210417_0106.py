# Generated by Django 2.2.13 on 2021-04-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_complain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('Reason', models.TextField(default=None, max_length=500)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('unapproved', 'UNAPPROVED'), ('decline', 'DECLINED')], default='Not Approved', max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='complain',
            name='complain_text',
            field=models.TextField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='address',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
