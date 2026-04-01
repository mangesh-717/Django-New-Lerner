from typing import Any
from django.db import models

# Create your models here.
class position(models.Model):
    title=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return  self.title
class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=4)
    mobile=models.CharField(max_length=15)


    # here we have applied foraign key relationship
    position=models.ForeignKey( position,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return  self.fullname
    


    