from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

# Create your views here.

def login(request):
    if request.method == "POST":
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count() #admin login
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count() #user login
        authoritycount=tbl_authority.objects.filter(authority_email=email,authority_password=password).count() #authority login
        hospitalcount=tbl_hospital.objects.filter(hospital_email=email,hospital_password=password).count() #hospital login

        if admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:homepage')
        elif usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('User:homepage')
        elif authoritycount>0:
                    authoritydata=tbl_authority.objects.get(authority_email=email,authority_password=password)
                    request.session['pid']=authoritydata.id
                    return redirect('Authority:homepage')      
        elif hospitalcount>0:
                            hospitaldata=tbl_hospital.objects.get(hospital_email=email,hospital_password=password)
                            request.session['hid']=hospitaldata.id
                            return redirect('Hospital:homepage')      
                
        else:
            return render(request, 'Guest/Login.html',{'msg':'Invalid Data'})
    
    else:
        return render(request, 'Guest/Login.html')


def userregistration(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get('txt_name')
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        password=request.POST.get('txt_password')
        place=tbl_place.objects.get(id=request.POST.get('selplace'))
        tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_photo=photo,place=place,user_password=password)
        return redirect('Guest:userregistration')
    else:
        return render(request, 'Guest/UserRegistration.html',{'dis':district})
    
def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))

    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})


def index(request):
    if request.method == "POST":
        return render(request, 'Guest/index.html')
    else:
        return render(request, 'Guest/index.html')