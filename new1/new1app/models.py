from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class student(models.Model):
    name= models.CharField(max_length=100)
    about= models.CharField(max_length=1000 , blank=True)
    email =models.EmailField()
    Users=models.ForeignKey(User,on_delete=models.SET_NULL , null=True , blank=True)# CASCADE SET_NULL SET_DEFAULT)
    photo=models.ImageField(upload_to='images/' , blank=True)
    # resume=models.FileField()
    def __str__(self) -> str:
        return  self.name