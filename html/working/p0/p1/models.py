from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10, null=True, blank=True)
    stname = models.CharField(max_length=10, null=True, blank=True)

    phone = models.BigIntegerField()
    email = models.EmailField()
    content = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)
