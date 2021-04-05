from django.shortcuts import render
from .models import Student
from django.contrib import messages
from .forms import stform
from django.views.generic import TemplateView

def stdisplay(request):
    results=Student.objects.all()
    return render(request,"index.html",{"Student":results})

def signup(request):
    template_name = 'homepage.html'
    return render(request, "homepage.html")

def stinsert(request):
    if request.method=="POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('stmobile') and request.POST.get('stgender'):
            savest=Student()
            savest.stname=request.POST.get('stname')
            savest.stemail = request.POST.get('stemail')
            savest.staddress = request.POST.get('staddress')
            savest.stmobile = request.POST.get('stmobile')
            savest.stgender = request.POST.get('stgender')
            savest.save()
            messages.success(request,"The Record"+savest.stname+"Is Saved Successfully...!")
            return render(request,"create.html",{})
    else:
        return render(request, "create.html", {})


def stedit(request,id):
    getstudentdetails=Student.objects.get(id=id)
    return render(request,'edit.html',{"Student":getstudentdetails})

def stupdate(request,id):
    stupdate=Student.objects.get(id=id)
    form=stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The Student Record Is Updated Successfully...!")
        return render(request,"edit.html",{"Student":stupdate})
    else:
        return render(request, "edit.html", {"Student":stupdate})


def stdel(request,id):
    delstudent=Student.objects.get(id=id)
    delstudent.delete()
    results = Student.objects.all()
    return render(request, "index.html",{"Student":results})