from django.db import models
from Admin.models import*


# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='Assets/Files/User/Photo/')
    user_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
      