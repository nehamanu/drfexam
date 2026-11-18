from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    employee_id=models.CharField(max_length=10)
    department=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    salary=models.IntegerField()
    image=models.ImageField(upload_to='media',null=True)

