from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10, null=True, blank=True)
    stname = models.CharField(max_length=20, null=True, blank=True)
    phone = models.BigIntegerField()
    age=models.IntegerField(blank=True , null=True)
    email = models.EmailField()
    content = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    

    def __str__(self) -> str:
        return 'Message from ' +self.name + '-' + self.email
    
    class Meta:
        ordering=['name']     #it will store records in ascending order of name
        verbose_name='killer_student'







