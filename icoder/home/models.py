from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    content=models.TextField()
    timeStamp=models.DateField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email