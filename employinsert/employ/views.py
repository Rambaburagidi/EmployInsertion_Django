from django.shortcuts import render
from .models import employ
from django.http import HttpResponse
# Create your views here.
def create(request):
    if request.method=="POST":
        userid=request.POST['userid']
        empname=request.POST['empname']
        empdeg=request.POST['empdeg']
        qualification=request.POST['qualification']
        gender=request.POST['gender']
        salary=request.POST['salary']
        email=request.POST['email']
        place=request.POST['place']
        contactno=request.POST['contactno']
        k=employ(userid=userid,empname=empname,empdeg=empdeg,qualification=qualification,gender=gender,salary=salary,email=email,place=place,contactno=contactno)
        k.save()
        return HttpResponse("record is inserted")
    return render(request,"employ.html")
