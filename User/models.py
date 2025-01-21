from django.db import models
from Guest.models import *

# Create your models here.
class tbl_request(models.Model):
   
    request_file=models.FileField(upload_to='Assets/Files/User/Photo/')
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)


class tbl_requestbody(models.Model):
    requestbody_status=models.IntegerField(default=0)
    request_id=models.ForeignKey(tbl_request,on_delete=models.CASCADE)
    authority_id=models.ForeignKey(tbl_authority,on_delete=models.CASCADE,null=True)
    hospital_id=models.ForeignKey(tbl_hospital,on_delete=models.CASCADE,null=True)