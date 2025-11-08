from django.http import HttpResponse
from django.shortcuts import render
from Employee.models import Employee
def home(request):
    emplyoee=Employee.objects.all()
    context={
        'emplyoee': emplyoee
    }
    return render(request,'home.html',context)