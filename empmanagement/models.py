from django.db import models

# Create your models here.

class Employee(models.Model):
    Emp_code=models.CharField(max_length=100)
    name=models.CharField(max_length=15)
    
    options=(
        ('DEVELOPER',"DEVELOPER"),
        ("HR MANAGER","HR MANAGER"),
        ("QUALITY ANALYST","QUALITY ANALYST"),
        ("UI_UX","UI_UX"),
    )
    
    position=models.CharField(max_length=30,choices=options)
    contact=models.IntegerField()
    city=models.CharField(max_length=34)
    salary=models.IntegerField()


    def __str__(self):
        return self.name