from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
from django.db import connection
cursor=connection.cursor()


def index(request):
    # projects=project.objects.all()
    projects=cursor.execute("Select * From portfolio_project;")
    # print(p)
    # for p in p:
    #     print(p.projectname)
    return render(request,'index.html',{'projects':projects})

def contact(request):
    projects=project.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        msg=Contact(name=name,email=email,message=message)
        msg.save()
        messages.success(request,"Thanks For Your Kind Response We will reach you as soon as possible")
        print(name,email,message)
        return render(request,'index.html',{'projects':projects})
    else:
        return render(request,'index.html',{'projects':projects})

    