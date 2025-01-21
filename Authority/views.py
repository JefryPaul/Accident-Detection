from django.shortcuts import render
from Admin.models import *
from User.models import *


# Create your views here.
def homepage(request):
    data=tbl_authority.objects.get(id=request.session['pid'])
    return render(request, 'Authority/HomePage.html',{'dat':data})

def myprofile(request):
    data=tbl_authority.objects.get(id=request.session['pid'])
    return render(request, 'Authority/Myprofile.html',{'dat':data})


def editprofile(request):
    data=tbl_authority.objects.get(id=request.session['pid'])
    if request.method=='POST':
        data.authority_name=request.POST.get('txt_name')
        data.authority_email=request.POST.get('txt_email')
        data.authority_address=request.POST.get('txt_address')
        data.authority_contact=request.POST.get('txt_contact')
        data.save()
        return render(request, 'Authority/EditProfile.html',{'msg':"Profile Updated"})
    else:
        return render(request, 'Authority/EditProfile.html',{'dat':data})

def changepassword(request):
    data=tbl_authority.objects.get(id=request.session['pid'])
    dbpass=data.authority_password
    print(dbpass)
    if request.method=='POST':
        oldpass=request.POST.get('txt_old')
        newpass=request.POST.get('txt_new')
        cpass=request.POST.get('txt_cpass')
        if dbpass==oldpass:
            if newpass==cpass:
                if dbpass==newpass:
                    return render(request,'Authority/ChangePassword.html',{'msg':"Already Used Try Another"})
                else:
                    data.authority_password=newpass
                    data.save()
                    return render(request,'Authority/ChangePassword.html',{'msg1':"Password Updated"})

                    # return redirect('Authority:myprofile')
            else:
                return render(request,'Authority/ChangePassword.html',{'msg':"Password Not Match"})
        else:
            return render(request,'Authority/ChangePassword.html',{'msg':"Incorrect Current Password"})  
        
    return render(request, 'Authority/ChangePassword.html')


def viewrequest(request):
    req=tbl_request.objects.all()
    return render(request, 'Authority/ViewRequest.html',{'dis':req})