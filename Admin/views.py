from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*

# Create your views here.
def district(request):
    dst=tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get('txt_district')
        tbl_district.objects.create(district_name=name)
        return render(request, 'Admin/District.html',{'dis':dst})
    else:
        return render(request, 'Admin/District.html',{'dis':dst})
    

def category(request):
    cat=tbl_category.objects.all()
    if request.method == "POST":        
        name=request.POST.get('txt_category')
        tbl_category.objects.create(category_name=name)
        return render(request, 'Admin/Category.html',{'cate':cat})
    else:
        return render(request, 'Admin/Category.html',{'cate':cat})


def subcategory(request):
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()

    if request.method == "POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategory=request.POST.get("txt_subcategory")
        tbl_subcategory.objects.create(category=category,subcategory_name=subcategory) 
        return redirect('Admin:subcategory')
    else:
        return render(request, 'Admin/Subcategory.html',{'category':category,'subcategory':subcategory})

def place(request):
    dis=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method == "POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        place=request.POST.get("txt_place")
        tbl_place.objects.create(district=district,place_name=place) 
        return redirect('Admin:place')
    else:
        return render(request, 'Admin/Place.html',{'district':dis,'place':place})
    
def deletedis(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:district')

def editdis(request,eid):
    data=tbl_district.objects.get(id=eid)
    if request.method=='POST':
        data.district_name=request.POST.get('txt_district')
        data.save()
        return redirect('Admin:district')
    else:
        return render(request, 'Admin/District.html',{'name':data})

def deletediss(request,didd):
    tbl_category.objects.get(id=didd).delete()
    return redirect('Admin:category')

def admin(request):
    cat=tbl_admin.objects.all()
    if request.method == "POST":        
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')
     
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        
        
        return render(request, 'Admin/admin.html',{'cate':cat})
    else:
        return render(request, 'Admin/admin.html',{'cate':cat})
    
def deletedisss(request,diddd):
    tbl_admin.objects.get(id=diddd).delete()
    return redirect('Admin:admin')


def deletedplace(request,diplace):
    tbl_place.objects.get(id=diplace).delete()
    return redirect('Admin:place')


def deletedsubcategory(request,disubcategory):
    tbl_subcategory.objects.get(id=disubcategory).delete()
    return redirect('Admin:subcategory')


def editplace(request,eid):
    dis=tbl_district.objects.all()
    data=tbl_place.objects.get(id=eid)
    if request.method=='POST':
        data.place_name=request.POST.get('txt_place')
        data.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        data.save()
        return redirect('Admin:place')
    else:
        return render(request, 'Admin/Place.html',{'name':data,'district':dis})
    
def editplace(request,eid):
    dis=tbl_district.objects.all()
    data=tbl_place.objects.get(id=eid)
    if request.method=='POST':
        data.place_name=request.POST.get('txt_place')
        data.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        data.save()
        return redirect('Admin:place')
    else:
        return render(request, 'Admin/Place.html',{'name':data,'district':dis})
    

def editsubcategory(request,eid):
    dis=tbl_category.objects.all()
    data=tbl_subcategory.objects.get(id=eid)
    if request.method=='POST':
        data.subcategory_name=request.POST.get('txt_subcategory')
        data.category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        data.save()
        return redirect('Admin:subcategory')
    else:
        return render(request, 'Admin/Subcategory.html',{'name':data,'category':dis})
    

def viewusers(request):
    users=tbl_user.objects.all()
    return render(request, 'Admin/ViewUsers.html',{'dis':users})



def deletedusers(request,did):
    tbl_user.objects.get(id=did).delete()
    return redirect('Admin:viewusers')

def homepage(request):
    return render(request, 'Admin/HomePage.html')

def authorityreg(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get('txt_name')
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        district=request.POST.get("seldistrict")
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")       
        password=request.POST.get('txt_password')
        place=tbl_place.objects.get(id=request.POST.get('selplace'))
        tbl_authority.objects.create(authority_name=name,authority_email=email,authority_contact=contact,authority_address=address,authority_district=district,authority_proof=proof,authority_photo=photo,place=place,authority_password=password)
        return redirect('Admin:authorityreg')
    else:
        return render(request, 'Admin/AuthorityReg.html',{'dis':district})
    

def hospitalreg(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get('txt_name')
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        district=request.POST.get("seldistrict")
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")       
        password=request.POST.get('txt_password')
        place=tbl_place.objects.get(id=request.POST.get('selplace'))
        tbl_hospital.objects.create(hospital_name=name,hospital_email=email,hospital_contact=contact,hospital_address=address,hospital_district=district,hospital_proof=proof,hospital_photo=photo,place=place,hospital_password=password)
        return redirect('Admin:hospitalreg')
    else:
        return render(request, 'Admin/HospitalReg.html',{'dis':district})
    
def viewauthority(request):
    authority=tbl_authority.objects.all()
    return render(request, 'Admin/ViewAuthority.html',{'dis':authority})

def accept(request,aid):
    auth=tbl_authority.objects.get(id=aid)
    auth.authority_status='1'
    auth.save()
    return redirect('Admin:viewauthority')
    
    
def reject(request,rid):
    auth=tbl_authority.objects.get(id=rid)
    auth.authority_status='2'
    auth.save()
    return redirect('Admin:viewauthority')
   

def viewhospital(request):
    hospital=tbl_hospital.objects.all()
    return render(request, 'Admin/ViewHospital.html',{'dis':hospital})


def haccept(request,haid):
    auth=tbl_hospital.objects.get(id=haid)
    auth.hospital_status='1'
    auth.save()
    return redirect('Admin:viewhospital')
    
    
def hreject(request,hrid):
    auth=tbl_hospital.objects.get(id=hrid)
    auth.hospital_status='2'
    auth.save()
    return redirect('Admin:viewhospital')

