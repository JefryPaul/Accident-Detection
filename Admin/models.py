from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_place(models.Model):
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
    place_name=models.CharField(max_length=30)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

class tbl_subcategory(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=30)

class tbl_authority(models.Model):
    authority_name=models.CharField(max_length=30)
    authority_email=models.CharField(max_length=30)
    authority_contact=models.CharField(max_length=30)
    authority_district=models.CharField(max_length=30)    
    authority_address=models.CharField(max_length=50)
    authority_photo=models.FileField(upload_to='Assets/Files/User/Photo/')
    authority_proof=models.FileField(upload_to='Assets/Files/User/Photo/')
    authority_password=models.CharField(max_length=30)
    authority_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
      

class tbl_hospital(models.Model):
    hospital_name=models.CharField(max_length=30)
    hospital_email=models.CharField(max_length=30)
    hospital_contact=models.CharField(max_length=30)
    hospital_district=models.CharField(max_length=30)    
    hospital_address=models.CharField(max_length=50)
    hospital_photo=models.FileField(upload_to='Assets/Files/User/Photo/')
    hospital_proof=models.FileField(upload_to='Assets/Files/User/Photo/')
    hospital_password=models.CharField(max_length=30)
    hospital_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)