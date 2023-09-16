from django.db import models

# Create your models here.
class employ(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=100)
    empdeg=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    salary=models.IntegerField()
    email=models.EmailField()
    place=models.CharField(max_length=100)
    contactno=models.BigIntegerField()

class Meta:
    db_table="employ"