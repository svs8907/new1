from django.shortcuts import render
def home(request):
    return render(request,'home.html',{'name':'VAIBHAV'})
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    return render(request,'results.html',{'results':val3})