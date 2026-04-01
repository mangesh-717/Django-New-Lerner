from django.db import models

# it is time to go in depth of django rest framework
    # here serilization on foraign key is going to start

class Colors(models.Model):
    color_name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.color_name



# Create your models here.
class Students(models.Model):
    color=models.ForeignKey(Colors,on_delete=models.CASCADE ,null=True,blank=True ,related_name="color")

    name=models.CharField(max_length=20)
    age=models.IntegerField()
    last_name=models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.name  
    