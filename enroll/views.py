from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegisteration
from .models import User
# Create your views here.
def addandshow(request):
    if request.method=='POST':
        fm=StudentRegisteration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            father=fm.cleaned_data['father_Name']
            adress=fm.cleaned_data['Address']
           
            reg=User(name=name,email=email,father_Name=father,Address=adress)
            reg.save()
            fm=StudentRegisteration()
    else:
        fm=StudentRegisteration()
    stud=User.objects.all()
    return render(request,"enroll/addandshow.html",{'form':fm,'stu':stud})

def updatedata(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')    