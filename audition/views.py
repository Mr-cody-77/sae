from django.shortcuts import render, HttpResponse
from audition.models import mydata


# Create your views here.
def home(request):
    return render(request, "home.html")
def form(request):
    try:
        if request.method=="POST":
            name = request.POST.get("name")
            roll = request.POST.get("roll")
            dept = request.POST.get("dept")
            phone = request.POST.get("phone")
            obj = mydata(name=name, roll=roll, dept = dept,phone=phone)
            obj.save()
    except Exception as e:
        pass
    return render(request, "new.html")

