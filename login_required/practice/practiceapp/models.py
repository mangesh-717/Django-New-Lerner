from django.db import models
# Create your models here.
class Studentttt(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    photo=models.FileField(upload_to='media/', blank=True)



