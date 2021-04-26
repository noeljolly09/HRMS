from django.db import models

# Create your models here.

class employeeDetails(models.Model):
    firstName = models.CharField(max_length=20,default=None)
    lastName = models.CharField(max_length=20,default=None)
    address = models.CharField(max_length=200,blank=False,default=None)
    email = models.EmailField(max_length=20,unique=True, blank=False,default=None)
    DOB = models.DateField(default=None)
    phoneNumber = models.BigIntegerField(default=None)
    salary = models.CharField(max_length=16,default='00,000.00')

class complain(models.Model):

    c_type = (('complain','COMPLAIN'),('suggestion','SUGGESTION'))
    date = models.DateField(default=None)
    Type = models.CharField(choices=c_type, default=None,max_length=10)
    complain_text = models.TextField(max_length=500,default=None)


class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    apply_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    Reason = models.TextField(max_length=500,default=None)
    employee = models.ForeignKey('employeeDetails',on_delete=models.CASCADE,default=None)
    status = models.CharField(choices=STATUS,max_length=15)
