from django.shortcuts import render
from Admin.models import *
from User.models import *

# Create your views here.

def homepage(request):
    data=tbl_hospital.objects.get(id=request.session['hid'])
    return render(request, 'Hospital/HomePage.html',{'dat':data})

def myprofile(request):
    data=tbl_hospital.objects.get(id=request.session['hid'])
    return render(request, 'Hospital/Myprofile.html',{'dat':data})

def editprofile(request):
    data=tbl_hospital.objects.get(id=request.session['hid'])
    if request.method=='POST':
        data.hospital_name=request.POST.get('txt_name')
        data.hospital_email=request.POST.get('txt_email')
        data.hospital_address=request.POST.get('txt_address')
        data.hospital_contact=request.POST.get('txt_contact')
        data.save()
        return render(request, 'Hospital/EditProfile.html',{'msg':"Profile Updated"})
    else:
        return render(request, 'Hospital/EditProfile.html',{'dat':data})


def changepassword(request):
    data=tbl_hospital.objects.get(id=request.session['pid'])
    dbpass=data.hospital_password
    print(dbpass)
    if request.method=='POST':
        oldpass=request.POST.get('txt_old')
        newpass=request.POST.get('txt_new')
        cpass=request.POST.get('txt_cpass')
        if dbpass==oldpass:
            if newpass==cpass:
                if dbpass==newpass:
                    return render(request,'Hospital/ChangePassword.html',{'msg':"Already Used Try Another"})
                else:
                    data.hospital_password=newpass
                    data.save()
                    return render(request,'Hospital/ChangePassword.html',{'msg1':"Password Updated"})

                    # return redirect('Hospital:myprofile')
            else:
                return render(request,'Hospital/ChangePassword.html',{'msg':"Password Not Match"})
        else:
            return render(request,'Hospital/ChangePassword.html',{'msg':"Incorrect Current Password"})  
        
    return render(request, 'Hospital/ChangePassword.html')

def viewrequest(request):
    req=tbl_request.objects.all()
    return render(request, 'Hospital/ViewRequest.html',{'dis':req})
