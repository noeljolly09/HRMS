from django.contrib import admin
from .models import employeeDetails,complain,Leave
# Register your models here.

admin.site.register(employeeDetails)
admin.site.register(complain)
admin.site.register(Leave)