from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    age=models.IntegerField(null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    image=models.FileField(null=True,blank=True)



    def __str__(self):
        return self.username


class Marks(models.Model):
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    maths =models.CharField(max_length=100)
    english=models.CharField(max_length=100)
    malayalam=models.CharField(max_length=100)
    hindi=models.CharField(max_length=100)        

    def __str__(self):
        return self.maths