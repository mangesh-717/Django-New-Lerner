from django.db import models

# Create your models here.
class student(models.Model):

    name= models.CharField(max_length=100)
    email =models.EmailField()
    photo=models.ImageField(upload_to='images/' , blank=True)
    # resume=models.FileField()