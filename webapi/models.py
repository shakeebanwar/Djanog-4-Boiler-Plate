from django.db import models

# Create your models here.

role = (

    ('superadmin','superadmin'),
    ('subadmin','subadmin')

)

class Super_AdminAccount(models.Model):

    SId = models.AutoField(primary_key=True)
    Fname=models.CharField(max_length=255, default="")
    Lname=models.CharField(max_length=255, default="")
    Email=models.EmailField(max_length=255, default="")
    Username=models.CharField(max_length=255, default="")
    Password=models.TextField(max_length=3000, default="")
    ContactNo=models.CharField(max_length=100, default="")
    Role = models.CharField(max_length=10,choices=role, default="subadmin") 
    Profile= models.ImageField(upload_to='SuperAdmin/',default="SuperAdmin/dummy.jpg")
    def __str__(self):
        return self.Fname