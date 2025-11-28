from django.db import models
from django.contrib import admin
# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length=20, help_text="Enter customer Name")
    age = models.IntegerField(help_text="Enter age between 18 to 22")
    address = models.CharField(max_length=50, help_text="Enter the Address")
    mobile_no = models.IntegerField(help_text="Enter the Mobile Number")

class customerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'age', 'address','mobile_no']
