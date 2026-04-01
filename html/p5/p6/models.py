from django.db import models

# Create your models here.
class studentdata(models.Model):

    name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    phon=models.IntegerField()
    email=models.EmailField()
    photo=models.ImageField(upload_to='student/' , blank=True)


    def __str__(self):
        return self.name