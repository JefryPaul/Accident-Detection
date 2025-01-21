from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method == "POST":
        a = request.POST.get("txtname1")
        b = request.POST.get("txtname2")
        c = int(a) + int(b)
        return render(request, 'Basics/Add.html', {'result':c})
    else:
        return render(request, 'Basics/Add.html')

def largest(request):
    if request.method == "POST":
        a = int(request.POST.get("txtname1"))
        b = int(request.POST.get("txtname2"))
        if a > b:
            return render(request, 'Basics/Largest.html', {'result':a})
        else:
            return render(request, 'Basics/Largest.html', {'result':b})
    else:
        return render(request,'Basics/Largest.html')

def calculator(request):
    if request.method=="POST":
        a = int(request.POST.get("txtname1"))
        b = int(request.POST.get("txtname2"))
        n=request.POST.get("btnsubmit")
        if n=="+":
            c=a+b
            return render(request, 'Basics/Calculator.html', {'result':c})
        elif n=="-":
            c=a-b
            return render(request, 'Basics/Calculator.html', {'result':c})
        elif n=="*":
            c=a*b
            return render(request, 'Basics/Calculator.html', {'result':c})
        elif n=="/":
            c=a/b
            return render(request, 'Basics/Calculator.html', {'result':c})
    else:
        return render(request,'Basics/Calculator.html')
def form(request):
        if request.method=="POST":
            k=request.POST.get("fname")+" "+request.POST.get("lname")
            p=request.POST.get("address")+" "+request.POST.get("email")+" "+request.POST.get("contact")
            s=request.POST.get("gender")
            if s=="M":
                q="Male"
            else:
                q="Female"
            return render(request, 'Basics/Form.html', {'result':k,'result1':p,'result2':q})            
        else:
            return render(request,'Basics/Form.html')


        


